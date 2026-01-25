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


def load_croissant_data(data_dir):
    """
    Loads Croissant JSON-LD files and converts them into spaCy training format.
    Returns training examples for NER (Named Entity Recognition).
    """
    training_data = []
    files = glob.glob(os.path.join(data_dir, "croissant_*.json"))
    
    print(f"Found {len(files)} Croissant files in {data_dir}")
    
    for file_path in files:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                
            # Extract Core Metadata
            term = data.get("name", "")
            context = data.get("description", "")
            identifier = data.get("https://schema.org/identifier", "")
            
            if not term or not context:
                continue
            
            # Create training example with the term as an entity in context
            # Format: (text, {"entities": [(start, end, label)]})
            if term.lower() in context.lower():
                start_idx = context.lower().find(term.lower())
                end_idx = start_idx + len(term)
                
                training_data.append((
                    context,
                    {"entities": [(start_idx, end_idx, "DISASTER_TERM")]}
                ))
            
            # Extract translations
            alternates = data.get("sc:alternateName", [])
            for alt in alternates:
                lang = alt.get("@language")
                translation = alt.get("@value")
                
                if not lang or not translation:
                    continue
                
                # Create synthetic training examples
                # Format: "The term X in {lang} is {translation}"
                synthetic_text = f"The disaster risk term '{term}' in {lang} is '{translation}'."
                
                # Mark both the original term and translation as entities
                entities = []
                
                # Find term position
                term_start = synthetic_text.find(f"'{term}'")
                if term_start != -1:
                    entities.append((term_start + 1, term_start + 1 + len(term), "DISASTER_TERM"))
                
                # Find translation position
                trans_start = synthetic_text.find(f"'{translation}'")
                if trans_start != -1:
                    entities.append((trans_start + 1, trans_start + 1 + len(translation), "TRANSLATION"))
                
                if entities:
                    training_data.append((synthetic_text, {"entities": entities}))
                    
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
    ner.add_label("DISASTER_TERM")
    ner.add_label("TRANSLATION")
    
    # Convert to spaCy Example format
    examples = []
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        examples.append(example)
    
    print(f"Training on {len(examples)} examples...")
    
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
    parser.add_argument("--output-dir", default="training/spacy_model", help="Output directory for trained model")
    parser.add_argument("--n-iter", type=int, default=30, help="Number of training iterations")
    parser.add_argument("--test", action="store_true", help="Run test after training")
    
    args = parser.parse_args()
    
    # Load data
    print("Loading training data...")
    training_data = load_croissant_data(args.data_dir)
    
    if not training_data:
        print("No training data found. Exiting.")
        return
    
    print(f"Loaded {len(training_data)} training examples")
    
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
