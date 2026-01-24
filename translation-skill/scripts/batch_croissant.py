import csv
import json
import argparse
import os
import sys

# Ensure we can import from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from croissant_generator import generate_croissant_metadata

def main():
    parser = argparse.ArgumentParser(description="Batch Generate Croissant Metadata from CSV")
    parser.add_argument("--input-file", dest="input_file", required=True, help="Path to input CSV (e.g., data/final_translations.csv)")
    parser.add_argument("--output-dir", dest="output_dir", default="output", help="Directory to save Croissant JSON files")
    parser.add_argument("--dataset-name", dest="dataset_name", default="Multilingual Vocabulary", help="Base name for the dataset")
    parser.add_argument("--description", default="A multilingual controlled vocabulary dataset.", help="Description of the dataset")
    parser.add_argument("--llm-model", dest="llm_model", default="gpt-oss:latest", help="Default LLM model if not in CSV")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: Input file {args.input_file} not found.")
        return

    os.makedirs(args.output_dir, exist_ok=True)
    
    # Read CSV and Group by Term
    terms_data = {} # term -> list of rows
    
    print(f"Reading {args.input_file}...")
    with open(args.input_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            term = row.get("term", "").strip()
            if term:
                if term not in terms_data:
                    terms_data[term] = []
                terms_data[term].append(row)
                
    print(f"Found {len(terms_data)} unique terms.")
    
    # Initialize Aggregated SKOS Content
    all_skos_content = "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
    all_skos_content += "@prefix dct: <http://purl.org/dc/terms/> .\n"
    all_skos_content += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    all_skos_content += "@prefix ex: <http://theminorityreport.org/vocab/> .\n\n"
    
    # Process each term
    for term, rows in terms_data.items():
        base_context = rows[0].get("context", "")
        
        # Build multilingual name list
        # Start with English (assuming term is English)
        name_list = [{"value": term, "lang": "en"}]
        
        # Filter valid translations
        lang_winners = {}
        models_used = set()
        
        for r in rows:
            lang = r.get("language")
            trans = r.get("translation")
            model = r.get("winning_model")
            consensus = r.get("consensus", "")
            
            if model:
                models_used.add(model)
            
            # Check for consensus or single model
            if lang and trans and ("Consensus reached" in consensus or "Single model" in consensus):
                # We expect only one winner per language per term for the final metadata
                if lang not in lang_winners:
                    lang_winners[lang] = {
                        "value": trans,
                        "lang": lang,
                        "model": model
                    }
        
        for lang_entry in lang_winners.values():
            name_list.append(lang_entry)
            
        # Serialize Name
        name_json = json.dumps(name_list)
        
        # Models string
        models_str = ",".join(list(models_used)) if models_used else args.llm_model
        
        # Clean description
        clean_desc = base_context.replace("\n", " ").strip()
        if len(clean_desc) > 200:
             clean_desc = clean_desc[:197] + "..."
             
        # Generate Metadata
        # We pass the full input file as the "data source" but ideally each Croissant might point to a slice?
        # For now, pointing to the master CSV is fine, referring to the specific term.
        
        metadata = generate_croissant_metadata(
            dataset_name=name_json,
            description=clean_desc,
            file_path=os.path.abspath(args.input_file), # Absolute path to data
            num_records=len(rows),
            llm_model=models_str
        )
        
        # Override creator list to only include models relevant to this term?
        # generate_croissant_metadata already auto-detects from the file if we let it, 
        # BUT we are passing the WHOLE file to it in the function call above inside generate_croissant_metadata's logic.
        # Actually generate_croissant_metadata re-reads the file to find models. 
        # This might be slightly inefficient for batch but it's fine for now. 
        # Wait, if we pass the whole file, it will find ALL models in the file, not just for this term.
        # So we should probably override the `creator` field in the metadata dict locally 
        # OR just accept that the dataset (the file) was created by all these models.
        # Since the Croissant file describes the DATASET (the CSV), listing all models is actually correct.
        
        # Save File
        import re
        # Sanitize: clean non-alphanumeric (keep hyphens/underscores if they were spaces)
        safe_term = re.sub(r'[^\w\s-]', '', term.strip().lower())
        safe_term = re.sub(r'[-\s]+', '_', safe_term)
        
        output_filename = f"croissant_{safe_term}.json"
        output_path = os.path.join(args.output_dir, output_filename)
        
        with open(output_path, "w") as f:
            json.dump(metadata, f, indent=2)
            
        print(f"Generated {output_path}")

        # --- SKOS Generation ---
        # Construct Concept Block
        term_id = safe_term
        
        concept_block = f"ex:{term_id} a skos:Concept ;\n"
        
        # English label and definition
        clean_def = base_context.replace('"', '\\"').replace("\n", " ").strip()
        concept_block += f'    skos:prefLabel "{term}"@en ;\n'
        concept_block += f'    skos:definition "{clean_def}"@en ;\n'
        
        # Translations as prefLabels
        for lang, entry in lang_winners.items():
            val = entry["value"].replace('"', '\\"').strip()
            concept_block += f'    skos:prefLabel "{val}"@{lang} ;\n'
            
        concept_block = concept_block.rstrip(" ;\n") + " .\n"
        
        # Append to Aggregated Content
        all_skos_content += concept_block + "\n"
        
        # Save Individual SKOS File (with prefixes)
        individual_ttl_prefixes = "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
        individual_ttl_prefixes += "@prefix dct: <http://purl.org/dc/terms/> .\n"
        individual_ttl_prefixes += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        individual_ttl_prefixes += "@prefix ex: <http://theminorityreport.org/vocab/> .\n\n"
        
        skos_filename = f"skos_{safe_term}.ttl"
        skos_path = os.path.join(args.output_dir, skos_filename)
        
        with open(skos_path, "w") as f:
            f.write(individual_ttl_prefixes + concept_block)
            
        print(f"Generated {skos_path}")

    # Write Aggregated SKOS File
    all_skos_path = os.path.join(args.output_dir, "all_vocab.ttl")
    with open(all_skos_path, "w") as f:
        f.write(all_skos_content)
    print(f"Generated Aggregated Vocabulary: {all_skos_path}")

    print("Batch generation complete.")

if __name__ == "__main__":
    main()
