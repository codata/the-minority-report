import csv
import json
import argparse
import os
import subprocess
import random
import datetime

# --- Mock LLM Interface ---
from ollama import Client
import requests
from bs4 import BeautifulSoup

OLLAMA_HOST = os.environ.get('OLLAMA_HOST', 'http://10.147.18.253:11434')

def mock_llm_call(prompt, model="gpt-oss:latest", is_json=True):
    """
    Calls the Ollama API using the OLLAMA_HOST environment variable.
    """
    try:
        client = Client(host=OLLAMA_HOST, timeout=600)
        
        # Call without format='json' to avoid empty responses if model is chatty
        response = client.generate(model=model, prompt=prompt, stream=False)
        response_text = response.get('response', '{}')
        
        # Log response
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        
        # Write Prompt Log
        with open(f"logs/prompt_{timestamp}.txt", "w") as f:
            f.write(prompt)
            
        # Write Response Log
        with open(f"logs/response_{timestamp}.txt", "w") as f:
            f.write(f"Raw Object:\n{str(response)}\n\nExtracted Text:\n{response_text}")
            
        return response_text
            
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return "{}"

# --- Main Logic ---

def load_prompt(path):
    with open(path, "r") as f:
        return f.read()

def scrape_url(url):
    """
    Scrapes term and context from a URL.
    """
    print(f"Scraping term from {url}...")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Extract Term (h1)
    term_elem = soup.find('h1')
    term = term_elem.get_text(strip=True) if term_elem else "Unknown Term"
    
    # Extract Definition (.field--name-body.lead)
    def_elem = soup.find('div', class_=lambda x: x and 'field--name-body' in x and 'lead' in x)
    
    if def_elem:
        p_elem = def_elem.find('p')
        context_text = p_elem.get_text(strip=True) if p_elem else def_elem.get_text(strip=True)
    else:
        def_elem = soup.find('div', class_=lambda x: x and 'field--name-body' in x)
        if def_elem:
            item_elem = def_elem.find('div', class_='field--item')
            context_text = item_elem.get_text(strip=True) if item_elem else def_elem.get_text(strip=True)
        else:
            context_text = "No definition found."
        
    print(f"Found Term: {term}")
    return term, context_text

def process_terms(rows, languages, models, voter_prompt_template, output_csv_path):
    """
    Processes a list of terms and returns translation results.
    """
    results = []
    if os.path.exists(output_csv_path):
        with open(output_csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                results.append(row)
                
    print(f"Loaded {len(results)} existing translations.")
    
    new_results = []
    for row in rows:
        term = row.get("term", "")
        context = row.get("context", "")
        print(f"\nProcessing Term: {term}")
        
        for model in models:
            print(f"  Using Model: {model}")
            prompt = voter_prompt_template.replace("{{target_languages}}", ", ".join(languages))
            prompt = prompt.replace("{{term}}", term)
            prompt = prompt.replace("{{scope_note}}", context)
            
            response_str = mock_llm_call(prompt, model=model).strip()
            
            response = {}
            if response_str:
                try:
                    response = json.loads(response_str)
                except json.JSONDecodeError:
                    import re
                    match = re.search(r'(\{.*\})', response_str, re.DOTALL)
                    if match:
                        try:
                            response = json.loads(match.group(1))
                        except:
                            pass

            if not response:
                print(f"    Failed to parse JSON for term '{term}'. Raw: {response_str[:50]}...")
            
            for lang in languages:
                lang_data = response.get(lang, {})
                if not isinstance(lang_data, dict):
                    if lang == "fr" and "translation" in response: 
                        lang_data = response 
                    else:
                        lang_data = {}

                translation = lang_data.get("translation", "")
                confidence = lang_data.get("confidence_score", 0.0)
                
                if not translation:
                    print(f"      [{lang}] No translation found in response.")

                print(f"      [{lang}] -> {translation} ({confidence})")

                new_results.append({
                    "term": term,
                    "context": context,
                    "translation": translation,
                    "language": lang,
                    "confidence": confidence,
                    "winning_model": model,
                    "version": "0.1"
                })

    existing_map = {(r["term"], r["language"], r["winning_model"]): i for i, r in enumerate(results)}
    for res in new_results:
        key = (res["term"], res["language"], res["winning_model"])
        if key in existing_map:
            results[existing_map[key]] = res
        else:
            results.append(res)
            
    return results

def main():

    parser = argparse.ArgumentParser(description="Orchestrator for Multilingual CV Skill")
    parser.add_argument("--input-file", "--input_file", dest="input_file", help="Path to source CSV")
    parser.add_argument("--url", help="URL to scrape term from (overrides input_file)")
    parser.add_argument("--output-dir", "--output_dir", dest="output_dir", default="data", help="Directory for output CSV")
    parser.add_argument("--languages", default="fr,es,de", help="Comma-separated target languages")
    parser.add_argument("--models", default="gpt-oss:latest", help="Comma-separated LLM models to use")
    
    args = parser.parse_args()
    
    # Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    prompts_dir = os.path.join(base_dir, "prompts")
    voter_prompt_template = load_prompt(os.path.join(prompts_dir, "voter_prompt.md"))
    
    languages = args.languages.split(",")
    models = args.models.split(",")
    output_csv_path = os.path.join(args.output_dir, "final_translations.csv")
    
    # Read Source
    rows = []
    if args.url:
        try:
            term, context_text = scrape_url(args.url)
            rows.append({"term": term, "context": context_text})
        except Exception as e:
            print(f"Error scraping URL: {e}")
            return
    elif args.input_file:
        with open(args.input_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    else:
        print("Error: Must provide either --input_file or --url")
        return
            
    results = process_terms(rows, languages, models, voter_prompt_template, output_csv_path)
    
    # Write Results
    fieldnames = ["term", "translation", "context", "language", "confidence", "winning_model", "version"]
    for res in results:
        res["version"] = "0.1"
        
    os.makedirs(args.output_dir, exist_ok=True)
    with open(output_csv_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
        
    print(f"\nSuccess! Translations written to {output_csv_path}")
    
    # 3. Serialize (Croissant)
    print("Generating Croissant Metadata...")
    # call croissant_generator.py
    # We assume it's in the same scripts/ dir
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "croissant_generator.py")
    
    cmd = ["python3", script_path, "--data-file", output_csv_path, "--output-dir", "output/"]
    
    # Check if we have a single term (URL mode or single row CSV) to name the dataset specificially
    # If we appended a new term, let's name the dataset after this new term for now as requested
    if len(rows) > 0:
        # Use the name/desc of the last processed term
        last_term = rows[-1].get("term", "Multilingual Vocabulary")
        last_context = rows[-1].get("context", "A multilingual controlled vocabulary dataset.")
        
        # Build multilingual name list
        name_list = [{"value": last_term, "lang": "en"}]
        
        # 2. Find translations for this term in results
        for res in results:
            if res.get("term") == last_term:
                lang = res.get("language")
                trans = res.get("translation")
                model = res.get("winning_model")
                if lang and trans:
                    name_list.append({
                        "value": trans,
                        "lang": lang,
                        "model": model
                    })
        
        # Serialize to JSON
        name_json = json.dumps(name_list)
        
        # Clean context for description (remove newlines, truncate if too long)
        clean_desc = last_context.replace("\n", " ").strip()
        if len(clean_desc) > 200:
             clean_desc = clean_desc[:197] + "..."
             
        cmd.extend(["--dataset-name", name_json])
        cmd.extend(["--description", clean_desc])
        cmd.extend(["--llm-model", args.models])

    if args.url:
        cmd.extend(["--source-url", args.url])
    elif args.input_file:
        cmd.extend(["--source-file", args.input_file])
        
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
