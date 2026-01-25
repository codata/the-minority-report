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


def load_croissant_data(data_dir, index_cache=None):
    """
    Loads Croissant JSON-LD files and converts them into spaCy training format.
    Returns training examples for NER (Named Entity Recognition).
    """
    training_data = []
    files = glob.glob(os.path.join(data_dir, "croissant_*.json"))
    
    print(f"Found {len(files)} Croissant files in {data_dir}")
    
    # Create lookup map from index cache for faster access
    # Map both term and URL to code
    term_to_code = {}
    url_to_code = {}
    
    if index_cache:
        print(f"Loaded {len(index_cache)} entries from index cache")
        for url, data in index_cache.items():
            code = data.get("code")
            term_name = data.get("term", "").lower()
            if code:
                if term_name:
                    term_to_code[term_name] = code
                url_to_code[url] = code # Full URL match as backup
    
    for file_path in files:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                
            # Extract Core Metadata
            term_raw = data.get("name", "")
            # Handle case where name is a list (multilingual names)
            if isinstance(term_raw, list):
                # Extract English name or first item
                term = next((item.get("value") for item in term_raw if isinstance(item, dict) and item.get("lang") == "en"), "")
                if not term and term_raw:
                    # Fallback to first item if no English found
                    term = term_raw[0].get("value", "") if isinstance(term_raw[0], dict) else str(term_raw[0])
            else:
                term = term_raw
                
            context = data.get("description", "")
            # Extract Identifier (HIPS Code)
            # Schema.org identifier or HIPS specific field
            identifier = data.get("https://schema.org/identifier", "")
            
            # Additional Lookup Strategy using Index Cache
            if not identifier and index_cache:
                # 1. Try lookup by Exact Term Name
                identifier = term_to_code.get(term.lower())
                
                # 2. Try lookup by Source URL (if present in metadata)
                if not identifier:
                    source_url = data.get("url", "")
                    if source_url:
                         identifier = url_to_code.get(source_url)
                         
            # Determine Label: Use HIPS code if available, else DISASTER_TERM
            main_label = identifier if identifier else "DISASTER_TERM"
            
            if not term or not context:
                continue
            
            # Create training example with the term as an entity in context
            # Format: (text, {"entities": [(start, end, label)]})
            if term.lower() in context.lower():
                start_idx = context.lower().find(term.lower())
                end_idx = start_idx + len(term)
                
                training_data.append((
                    context,
                    {"entities": [(start_idx, end_idx, main_label)]}
                ))
            
            # Language Mapping for nicer sentences
            lang_names = {
                "en": "English", "fr": "French", "es": "Spanish", "ru": "Russian", 
                "ar": "Arabic", "zh": "Chinese", "de": "German",
                "it": "Italian", "pt": "Portuguese", "ja": "Japanese",
                "ko": "Korean", "hi": "Hindi", "bn": "Bengali",
                "ur": "Urdu", "tr": "Turkish", "vi": "Vietnamese"
            }

            # Extract translations
            alternates = data.get("sc:alternateName", [])
            for alt in alternates:
                lang_code = alt.get("@language")
                translation = alt.get("@value")
                
                if not lang_code or not translation:
                    continue
                
                lang_name = lang_names.get(lang_code, lang_code.upper())
                
                # Create synthetic training examples
                # WE CONSTRUCT THE SENTENCE TO CALCULATE EXACT OFFSETS AND AVOID OVERLAP
                # Template: "The disaster risk term in English for {term} and translation in {Lang} ({code}) is {translation}."
                
                # Parts of the sentence
                p1 = "The disaster risk term in English for "
                p2 = f" and translation in {lang_name} ({lang_code}) is "
                p3 = "."
                
                # Full Text
                text = f"{p1}{term}{p2}{translation}{p3}"
                
                # Indices
                term_start = len(p1)
                term_end = term_start + len(term)
                
                trans_start = term_end + len(p2)
                trans_end = trans_start + len(translation)
                
                entities = []
                # Entity 1: Term (with HIPS code label)
                entities.append((term_start, term_end, main_label))
                
                # Entity 2: Translation (TR-{HIPS_CODE})
                tr_label = f"TR-{main_label}"
                entities.append((trans_start, trans_end, tr_label))
                
                training_data.append((
                    text,
                    {"entities": entities}
                ))
                
                # Optional: Add a variation with just the translation to be robust
                # "The {Lang} word for this concept is {translation}."
                p1_v2 = f"The {lang_name} word for this concept is "
                p2_v2 = "."
                text_v2 = f"{p1_v2}{translation}{p2_v2}"
                
                training_data.append((
                    text_v2,
                    {"entities": [(len(p1_v2), len(p1_v2) + len(translation), tr_label)]}
                ))
                
                # Natural Language Templates (Language-Specific)
                # Helps the model recognize terms in real context like definitions
                nl_templates = {
                    "it": ["Con il termine {trans} si intende...", "La definizione di {trans} è..."],
                    "fr": ["Le terme {trans} désigne...", "La définition de {trans} est..."],
                    "es": ["El término {trans} se refiere a...", "La definición de {trans} es..."],
                    "ru": ["Термин {trans} означает...", "Определение {trans}:"],
                    "en": ["The term {trans} refers to...", "Definition of {trans}:"],
                    "de": ["Der Begriff {trans} bezeichnet...", "Definition von {trans}:"],
                }
                
                # Add natural language example if template exists
                if lang_code in nl_templates:
                    for tmpl in nl_templates[lang_code]:
                        # Construct: "Con il termine cyberbullismo si intende..."
                        
                        # Split template by {trans} placeholder
                        parts = tmpl.split("{trans}")
                        if len(parts) == 2:
                             prefix_part = parts[0]
                             suffix_part = parts[1]
                             
                             nl_text = f"{prefix_part}{translation}{suffix_part}"
                             
                             # Entity: Translation (TR-{HIPS_CODE})
                             t_start = len(prefix_part)
                             t_end = t_start + len(translation)
                             
                             training_data.append((
                                 nl_text,
                                 {"entities": [(t_start, t_end, tr_label)]}
                             ))
                else: 
                     # Generic fallback
                     fallback = f"The term {translation} means..."
                     training_data.append((
                         fallback,
                         {"entities": [(9, 9 + len(translation), tr_label)]}
                     ))

                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return training_data


def train_spacy_model(training_data, output_dir, n_iter=30):
    """
    Train a spaCy NER model on the disaster risk terminology data.
    """
    # Create blank English model
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


def main():
    parser = argparse.ArgumentParser(description="Train spaCy NER model for disaster terminology")
    parser.add_argument("--data-dir", default="output", help="Directory containing Croissant JSON files")
    parser.add_argument("--index-file", help="Path to index cache JSON file for HIPS code lookup")
    parser.add_argument("--output-dir", default="training/spacy_model", help="Output directory for trained model")
    parser.add_argument("--n-iter", type=int, default=30, help="Number of training iterations")
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
    
    # Save training data for inspection
    # Force save to training/data/ relative to where we run it
    debug_dir = os.path.join("training", "data")
    if not os.path.exists(debug_dir):
        # Maybe we are inside training dir?
        if os.path.basename(os.getcwd()) == "training":
             debug_dir = "data"
        else:
             os.makedirs(debug_dir, exist_ok=True)
             
    debug_file = os.path.join(debug_dir, "training_data_dump.json")
    
    print(f"Saving training data snapshot to {debug_file}...")
    with open(debug_file, "w") as f:
        # Convert set/tuple to list/dict for JSON serialization
        serializable_data = []
        for text, annotations in training_data:
            entities = annotations.get("entities", [])
            # Convert entities to [start, end, label]
            serializable_data.append({
                "text": text,
                "entities": [[e[0], e[1], e[2]] for e in entities]
            })
        json.dump(serializable_data, f, indent=2)
    
    # Train model
    nlp = train_spacy_model(training_data, args.output_dir, args.n_iter)
    
    # Test if requested
    if args.test:
        test_texts = [
            "A thunderstorm is a meteorological phenomenon.",
            "The term drought in French is sécheresse.",
            "Flooding can cause significant damage to infrastructure.",
        ]
        test_model(nlp, test_texts)
    
    print("\n✓ Training complete!")
    print(f"Load the model with: nlp = spacy.load('{args.output_dir}')")


if __name__ == "__main__":
    main()
