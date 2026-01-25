#!/usr/bin/env python3
"""
Augment Croissant datasets with LLM-generated training examples.
Scalable solution to avoid hardcoded templates.
"""

import json
import glob
import os
import sys
import argparse
import time
from pathlib import Path

# Add translation-skill scripts to path to import orchestrator
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
orchestrator_path = os.path.join(project_root, "translation-skill", "scripts")
sys.path.append(orchestrator_path)

try:
    from orchestrator import mock_llm_call, repair_json
except ImportError:
    print("Error: Could not import orchestrator.py. check paths.")
    sys.exit(1)

def generate_examples(term, language, model="gpt-oss:latest", num_examples=3):
    """
    Generates diverse sentences containing the term in the target language.
    """
    prompt = f"""
    You are a linguistic expert helper.
    Task: Generate {num_examples} natural, diverse sentences in {language} that include the exact term '{term}'.
    
    Rules:
    1. The sentences should be varied (definitions, usage in context, questions).
    2. The term '{term}' must appear EXACTLY as written (same casing usually, unless grammar strictly forbids).
    3. Do NOT include the English translation unless it's natural for that language (e.g. loanwords).
    4. Return ONLY a JSON list of strings.
    
    Example Output:
    ["Sentence 1...", "Sentence 2...", "Sentence 3..."]
    """
    
    response = mock_llm_call(prompt, model=model)
    
    try:
        examples = json.loads(response)
        if isinstance(examples, list):
            return [e for e in examples if isinstance(e, str)]
    except json.JSONDecodeError:
        # Try repair
        repaired = repair_json(response)
        try:
            examples = json.loads(repaired)
            if isinstance(examples, list):
                return [e for e in examples if isinstance(e, str)]
        except:
            pass
            
    # Fallback: Split by newline if it looks like a list
    lines = response.strip().split('\n')
    clean_lines = []
    for line in lines:
        line = line.strip().lstrip('-').lstrip('1.').lstrip('"').rstrip('"').strip()
        if line and len(line) > 5:
            clean_lines.append(line)
            
    return clean_lines[:num_examples]

def process_file(file_path, model, limit=None):
    print(f"Processing {file_path}...")
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            
        changed = False
        
        # We need to find the translations.
        # In our Croissant, they are in sc:alternateName or we iterate sc:alternateName?
        # The structure is:
        # "sc:alternateName": [ {"@value": "...", "@language": "..."}, ... ]
        
        alternates = data.get("sc:alternateName", [])
        
        count = 0
        for alt in alternates:
            if limit and count >= limit:
                break
                
            lang = alt.get("@language")
            term = alt.get("@value")
            
            # Skip if examples already exist (to avoid re-generating expensive LLM calls)
            if "sc:example" in alt and alt["sc:example"]:
                continue
                
            if not lang or not term:
                continue
                
            # Skip English if we assume the main Description covers it, 
            # BUT we might want English examples too for robustness?
            # Let's generate for ALL languages including EN.
            
            print(f"  generating examples for '{term}' ({lang})...")
            examples = generate_examples(term, lang, model=model)
            
            if examples:
                print(f"    ✓ Generated {len(examples)} examples.")
                alt["sc:example"] = examples
                changed = True
                count += 1
            else:
                print(f"    ⚠️ No examples generated.")
                
        if changed:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2)
            print("  Saved updates.")
        else:
            print("  No changes necessary.")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Augment Croissant data with LLM examples")
    parser.add_argument("--data-dir", default="output", help="Directory with Croissant files")
    parser.add_argument("--file", help="Specific file to process (overrides --data-dir)")
    parser.add_argument("--model", default="gpt-oss:latest", help="LLM model to use")
    parser.add_argument("--limit", type=int, default=None, help="Limit examples per file (for testing)")
    
    args = parser.parse_args()
    
    if args.file:
        files = [args.file]
    else:
        files = glob.glob(os.path.join(args.data_dir, "croissant_*.json"))
        
    print(f"Found {len(files)} files to process.")
    
    for f in files:
        process_file(f, args.model, args.limit)

if __name__ == "__main__":
    main()
