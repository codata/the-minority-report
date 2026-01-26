#!/usr/bin/env python3
"""
Train a spaCy NER model to recognize disaster risk terminology and their translations.
This creates a lightweight, production-ready model for term extraction and translation.
"""

import json
import glob
import os
import argparse
import random
from pathlib import Path
import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding


import concurrent.futures
import multiprocessing

# Global helpers for multiprocessing (must be picklable)
def process_single_croissant_file(file_path, index_cache_data=None):
    """
    Process a single Croissant file and return training examples.
    Defined at module level for pickling.
    """
    local_data = []
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            
        # Extract Core Metadata
        term_raw = data.get("name", "")
        if isinstance(term_raw, list):
            term = next((item.get("value") for item in term_raw if isinstance(item, dict) and item.get("lang") == "en"), "")
            if not term and term_raw:
                term = term_raw[0].get("value", "") if isinstance(term_raw[0], dict) else str(term_raw[0])
        else:
            term = term_raw
            
        context = data.get("description", "")
        identifier = data.get("https://schema.org/identifier", "")
        
        # Determine Label
        main_label = f"HIPS_{identifier}" if identifier else "DISASTER_TERM"
        
        if not term or not context:
            return []
        
        # Example 1: Term in context
        if term.lower() in context.lower():
            start_idx = context.lower().find(term.lower())
            end_idx = start_idx + len(term)
            time_start = 0 
            # Find all? For now just first is fine or maybe all?
            # Let's keep original logic: simple find.
            local_data.append((
                context,
                {"entities": [(start_idx, end_idx, main_label)]}
            ))
        
        # Language Mapping
        lang_names = {
            "en": "English", "fr": "French", "es": "Spanish", "ru": "Russian", 
            "ar": "Arabic", "zh": "Chinese", "de": "German",
            "it": "Italian", "pt": "Portuguese", "ja": "Japanese",
            "ko": "Korean", "hi": "Hindi", "bn": "Bengali",
            "ur": "Urdu", "tr": "Turkish", "vi": "Vietnamese"
        }

        # Natural Language Templates (Language-Specific)
        nl_templates = {
            "it": ["Con il termine {trans} si intende...", "La definizione di {trans} è..."],
            "fr": ["Le terme {trans} désigne...", "La définition de {trans} est..."],
            "es": ["El término {trans} se refiere a...", "La definición de {trans} es..."],
            "ru": ["Термин {trans} означает...", "Определение {trans}:"],
            "en": ["The term {trans} refers to...", "Definition of {trans}:"],
            "de": ["Der Begriff {trans} bezeichnet...", "Definition von {trans}:"],
        }
        
        # Intro words for negative examples (simple approach)
        intro_words = {
             "nl": ["Maar ", "Echter "],
             "en": ["However ", "But "]
        }

        # Extract translations
        alternates = data.get("sc:alternateName", [])
        for alt in alternates:
            lang_code = alt.get("@language")
            translation = alt.get("@value")
            
            if not lang_code or not translation:
                continue
            
            lang_name = lang_names.get(lang_code, lang_code.upper())
            
            # Check for Augmentation Data (LLM Examples)
            examples = alt.get("sc:example", [])
            augment_examples_found = False
            
            if examples:
                if isinstance(examples, str):
                    examples = [examples]
                    
                for ex_text in examples:
                    ex_entities = []
                    start_search = 0
                    
                    while True:
                        idx = ex_text.lower().find(translation.lower(), start_search)
                        if idx == -1:
                            break
                            
                        end_idx = idx + len(translation)
                        tr_label = f"{main_label}_TR_{lang_code.upper()}"
                        ex_entities.append((idx, end_idx, tr_label))
                        
                        start_search = end_idx
                        
                    if ex_entities:
                       local_data.append((
                           ex_text,
                           {"entities": ex_entities}
                       ))
                       augment_examples_found = True

            if augment_examples_found:
                continue

            # Synthetic Training Examples
            p1 = "The disaster risk term in English for "
            p2 = f" and translation in {lang_name} ({lang_code}) is "
            p3 = " ."
            text = f"{p1}{term}{p2}{translation}{p3}"
            
            term_start = len(p1)
            term_end = term_start + len(term)
            trans_start = term_end + len(p2)
            trans_end = trans_start + len(translation)
            
            tr_label = f"{main_label}_TR_{lang_code.upper()}"
            
            local_data.append((
                text,
                {"entities": [
                    (term_start, term_end, main_label),
                    (trans_start, trans_end, tr_label)
                ]}
            ))
            
            # Variation
            p1_v2 = f"The {lang_name} word for this concept is "
            text_v2 = f"{p1_v2}{translation} ."
            local_data.append((
                text_v2,
                {"entities": [(len(p1_v2), len(p1_v2) + len(translation), tr_label)]}
            ))
            
            # Templates
            if lang_code in nl_templates:
                for tmpl in nl_templates[lang_code]:
                    parts = tmpl.split("{trans}")
                    if len(parts) == 2:
                         nl_text = f"{parts[0]}{translation}{parts[1]}"
                         t_start = len(parts[0])
                         t_end = t_start + len(translation)
                         local_data.append((
                             nl_text,
                             {"entities": [(t_start, t_end, tr_label)]}
                         ))
                         
            # Intro words "negative"
            if lang_code in intro_words:
                 for intro in intro_words[lang_code]:
                     text_intro = f"{intro}{translation} ."
                     t_start = len(intro)
                     t_end = t_start + len(translation)
                     local_data.append((
                         text_intro,
                         {"entities": [(t_start, t_end, tr_label)]}
                     ))
            else:
                 # Generic fallback
                 fallback = f"The term {translation} means..."
                 local_data.append((
                     fallback,
                     {"entities": [(9, 9 + len(translation), tr_label)]}
                 ))
                 
        return local_data
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def load_croissant_data(data_dir, index_cache=None):
    """
    Loads Croissant JSON-LD files and converts them into spaCy training format.
    Uses MULTIPROCESSING to utilize all cores.
    """
    training_data = []
    files = glob.glob(os.path.join(data_dir, "croissant_*.json"))
    
    print(f"Found {len(files)} Croissant files in {data_dir}")
    print(f"Processing using {multiprocessing.cpu_count()} cores...")
    
    # We ignore index_cache in the helper for simplicity/pickling, 
    # as most data is now self-contained in Croissant files and their IDs.
    # If strictly needed, checking index_cache logic would need to be moved inside or passed safely.
    # The current `process_single_croissant_file` relies on identifier inside file.
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Pass index_cache_data to the worker function if it were to be used there.
        # For now, it's passed but not used in process_single_croissant_file as per instruction.
        results = list(executor.map(process_single_croissant_file, files, [index_cache]*len(files)))
        
    for res in results:
        training_data.extend(res)
    
    return training_data


def train_spacy_model(training_data, output_dir, n_iter=30):
    """
    Train a spaCy NER model on the disaster risk terminology data.
    """
    # Check for GPU
    try:
        spacy.require_gpu()
        print("🚀 GPU detected and enabled for training!")
    except Exception as e:
        print(f"🖥️  GPU activation failed: {e}")
        print("    (Using CPU. Ensure 'cupy-cudaXX' is installed matches your CUDA version)")

    # Create blank Multilingual model
    # Use 'xx' for multi-language support (requires spacy-xx/multi-lang support)
    try:
        nlp = spacy.blank("xx")
        print("🌍 Using multilingual 'xx' base model.")
    except Exception:
        print("⚠️  Multilingual 'xx' model not found. Fallback to 'en'.")
        print("    Install it via: python -m spacy download xx_ent_wiki_sm (or similar if needed)")
        nlp = spacy.blank("en")
    
    # Add NER pipeline component
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")
    
    
    # Add labels
    # We now add labels dynamically based on the training data
    # ner.add_label("DISASTER_TERM") # Replaced by dynamic HIPS codes
    ner.add_label("TRANSLATION")
    
    # Convert to spaCy Example format
    examples = []
    labels = set()
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        examples.append(example)
        
        # Collect all unique labels to add to NER
        for ent in annotations.get("entities", []):
            labels.add(ent[2])
            
    # Add all discovered labels (HIPS codes)
    for label in labels:
        ner.add_label(label)
    
    print(f"Training on {len(examples)} examples with {len(labels)} unique labels (HIPS codes)...")
    
    # Disable other pipeline components during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.initialize()
        
        # Training loop
        for iteration in range(n_iter):
            random.shuffle(examples)
            losses = {}
            
            # Batch the examples
            batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
            
            for batch in batches:
                nlp.update(batch, drop=0.5, losses=losses, sgd=optimizer)
            
            print(f"Iteration {iteration + 1}/{n_iter} - Loss: {losses.get('ner', 0):.2f}")
    
    # Save model
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    nlp.to_disk(output_path)
    print(f"Model saved to {output_path}")
    
    return nlp


def test_model(nlp, test_texts):
    """
    Test the trained model on sample texts.
    """
    print("\n=== Testing Model ===")
    for text in test_texts:
        doc = nlp(text)
        print(f"\nText: {text}")
        print("Entities found:")
        for ent in doc.ents:
            print(f"  - {ent.text} ({ent.label_})")


def train_worker(args_pack):
    """
    Worker function for parallel training.
    """
    training_data, output_dir, n_iter, seed, job_id = args_pack
    
    # Set seed for reproducibility/variance
    random.seed(seed)
    spacy.util.fix_random_seed(seed)
    
    print(f"[Job {job_id}] Starting training with seed {seed}...")
    
    # Train
    nlp = train_spacy_model(training_data, output_dir, n_iter)
    
    # We can return the path or the loss or the model itself (if small)
    # But for simplicity, let's just return the directory and maybe a metric?
    # Since train_spacy_model doesn't return loss, let's trust it saved to disk.
    # Actually, proper selection requires evaluation.
    # For now, we will perform a 'Best of N' selection?
    # Or just let them save to different folders.
    
    return output_dir

def main():
    parser = argparse.ArgumentParser(description="Train spaCy NER model for disaster terminology")
    parser.add_argument("--data-dir", default="output", help="Directory containing Croissant JSON files")
    parser.add_argument("--index-file", help="Path to index cache JSON file for HIPS code lookup")
    parser.add_argument("--output-dir", default="training/spacy_model", help="Output directory for trained model")
    parser.add_argument("--n-iter", type=int, default=30, help="Number of training iterations")
    parser.add_argument("--n-jobs", type=int, default=1, help="Number of parallel training jobs (uses more CPUs)")
    parser.add_argument("--test", action="store_true", help="Run test after training")
    
    args = parser.parse_args()
    
    # Load Index Cache if provided
    index_cache = {}
    if args.index_file and os.path.exists(args.index_file):
        print(f"Loading index cache from {args.index_file}...")
        try:
            with open(args.index_file, "r") as f:
                index_cache = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load index file: {e}")
    
    # Load data
    print("Loading training data...")
    training_data = load_croissant_data(args.data_dir, index_cache=index_cache)
    
    if not training_data:
        print("No training data found. Exiting.")
        return
    
    print(f"Loaded {len(training_data)} training examples")
    
    # Parallel Training Logic
    if args.n_jobs > 1:
        print(f"\n🚀 Launching {args.n_jobs} parallel training jobs to utilize CPU cores!")
        print("This will train multiple models with different seeds and could be used for ensembling or finding the best model.\n")
        
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.n_jobs) as executor:
            futures = []
            for i in range(args.n_jobs):
                # Create unique output dir for each job
                job_output_dir = os.path.join(args.output_dir, f"run_{i}")
                seed = random.randint(1000, 9999)
                
                # Submit job
                # Note: Passing large training_data might be overhead if standard pickling is used,
                # but on Linux memory is often shared via fork.
                futures.append(
                    executor.submit(train_worker, (training_data, job_output_dir, args.n_iter, seed, i))
                )
            
            # Wait for completion
            for future in concurrent.futures.as_completed(futures):
                try:
                    res_dir = future.result()
                    print(f"✓ Job completed. Model saved to {res_dir}")
                except Exception as e:
                    print(f"❌ Job failed: {e}")
                    
        print(f"\nAll parallel jobs finished. Inspect {args.output_dir}/run_* for results.")
        # Optionally, we could symlink the 'run_0' to main output, or leave it to user.
        # Let's verify the first run for the test.
        final_model_dir = os.path.join(args.output_dir, "run_0")
        
    else:
        # Single Job
        nlp = train_spacy_model(training_data, args.output_dir, args.n_iter)
        final_model_dir = args.output_dir

    # Test if requested (Test the "primary" model, usually the first one or the only one)
    if args.test:
        print(f"\nTesting model from: {final_model_dir}")
        try:
            nlp = spacy.load(final_model_dir)
            test_texts = [
                "A thunderstorm is a meteorological phenomenon.",
                "The term drought in French is sécheresse.",
                "Flooding can cause significant damage to infrastructure.",
            ]
            test_model(nlp, test_texts)
        except Exception as e:
            print(f"Could not load model for testing: {e}")
    
    print("\n✓ Training complete!")
    if args.n_jobs > 1:
         print(f"Models are located in subdirectories of: {args.output_dir}")
    else:
         print(f"Load the model with: nlp = spacy.load('{args.output_dir}')")


if __name__ == "__main__":
    multiprocessing.set_start_method("fork", force=True) # efficient for Linux
    main()
