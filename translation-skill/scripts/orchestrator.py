import csv
import json
import argparse
import os
import subprocess
import random
import datetime
import time

import concurrent.futures

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

def repair_json(json_str):
    """
    Attempts to repair common JSON malformations from LLMs.
    """
    import re
    # Fix 1: Remove quotes after numbers (e.g. 0.96"})
    # Look for number followed immediately by quote then } or , or ]
    json_str = re.sub(r'(\d+(?:\.\d+)?)"\s*([,}\]])', r'\1\2', json_str)
    
    # Fix 2: Unescaped quotes inside strings? (Harder to do safely with regex)
    
    return json_str

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
        
    print(f"Description: {context_text}")
    return term, context_text

def scrape_index_page(index_url):
    """
    Scrapes the index page for all concept URLs matching the pattern.
    """
    print(f"Scraping index page: {index_url}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(index_url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching index page: {e}")
        return []
        
    soup = BeautifulSoup(response.text, "html.parser")
    # Base pattern based on inspection: /understanding-disaster-risk/terminology/hips/
    # We look for all 'a' tags with href containing this pattern
    links = set()
    base_domain = "https://www.preventionweb.net"
    
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/understanding-disaster-risk/terminology/hips/" in href:
            # Ensure full URL
            if href.startswith("/"):
                full_url = base_domain + href
            else:
                full_url = href
            
            # Simple validation: it should end with code usually, but let's just accept unique URLs that match the path
            links.add(full_url)
            
    print(f"Found {len(links)} unique concept URLs.")
    return list(links)

def _query_model(term, context, languages, model, voter_prompt_template):
    """Helper to query a single model and return parsed results."""
    print(f"  Using Model: {model}")
    prompt = voter_prompt_template.replace("{{target_languages}}", ", ".join(languages))
    prompt = prompt.replace("{{term}}", term)
    prompt = prompt.replace("{{scope_note}}", context)
    
    response_str = mock_llm_call(prompt, model=model).strip()
    
    response = {}
    response = {}
    if response_str:
        try:
            response = json.loads(response_str)
        except json.JSONDecodeError:
            print(f"    [{model}] JSON Parse Error. Attempting repair...")
            # 1. Try extracting greedy JSON object
            import re
            match = re.search(r'(\{.*\})', response_str, re.DOTALL)
            if match:
                candidate = match.group(1)
                try:
                    response = json.loads(candidate)
                    print(f"    [{model}] Repair successful (regex extraction).")
                except json.JSONDecodeError:
                     # 2. Try repair function
                     repaired = repair_json(candidate)
                     try:
                         response = json.loads(repaired)
                         print(f"    [{model}] Repair successful (regex + repair_json).")
                     except json.JSONDecodeError:
                         print(f"    [{model}] Repair failed after regex extraction.")
            else:
                 # Try repairing the whole string
                 repaired = repair_json(response_str)
                 try:
                     response = json.loads(repaired)
                     print(f"    [{model}] Repair successful (full string repair).")
                 except:
                     pass

    if not response:
        print(f"    [{model}] Failed to parse JSON for term '{term}'. Raw: {response_str[:50]}...")
        return []
    
    model_results = []
    for lang in languages:
        lang_data = response.get(lang, {})
        if not isinstance(lang_data, dict):
            if lang == "fr" and "translation" in response: 
                lang_data = response 
            else:
                lang_data = {}

        translation = lang_data.get("translation", "")
        confidence = lang_data.get("confidence_score", 0.0)
        
        if translation:
            model_results.append({
                "term": term,
                "context": context,
                "translation": translation,
                "language": lang,
                "confidence": confidence,
                "winning_model": model,
                "version": "0.1"
            })
        else:
            print(f"      [{lang}] No translation found in response from {model}.")
            
    return model_results

def _arbitrate_model(term, context, candidates, model, arbitrator_prompt_template):
    """Helper to query a model for arbitration."""
    print(f"  [Arbitration] Askiing Model: {model}")
    candidates_list = "\n".join([f"- {c}" for c in candidates])
    
    prompt = arbitrator_prompt_template.replace("{{term}}", term)
    prompt = prompt.replace("{{scope_note}}", context)
    prompt = prompt.replace("{{candidates}}", candidates_list)
    
    response_str = mock_llm_call(prompt, model=model).strip()
    
    selected = ""
    if response_str:
        try:
             # Try parse
             data = json.loads(response_str)
             selected = data.get("selected_translation", "")
        except:
             # Try repair
             repaired = repair_json(response_str)
             try:
                 data = json.loads(repaired)
                 selected = data.get("selected_translation", "")
             except:
                 # Try regex
                 import re
                 match = re.search(r'(\{.*\})', response_str, re.DOTALL)
                 if match:
                     try:
                         data = json.loads(match.group(1))
                         selected = data.get("selected_translation", "")
                     except:
                         pass
    
    if selected:
        print(f"    [{model}] voted for: {selected}")
    else:
        print(f"    [{model}] failed to vote.")
        
    return selected

def process_terms(rows, languages, models, voter_prompt_template, arbitrator_prompt_template, output_csv_path):
    """
    Processes a list of terms and returns translation results with consensus logic.
    A translation is only accepted if at least 2 models agree on it (case-insensitive).
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
        
        # Collect raw responses for this term
        raw_results = [] 
        
        # Execute model queries in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(models)) as executor:
            future_to_model = {
                executor.submit(_query_model, term, context, languages, model, voter_prompt_template): model 
                for model in models
            }
            
            for future in concurrent.futures.as_completed(future_to_model):
                try:
                    data = future.result()
                    raw_results.extend(data)
                except Exception as exc:
                    model_name = future_to_model[future]
                    print(f"Model {model_name} generated an exception: {exc}")

        # Apply Consensus Logic per language
        for lang in languages:
            lang_raw = [r for r in raw_results if r["language"] == lang]
            
            if len(models) == 1:
                print(f"    Single model used for [{lang}]. Skipping consensus.")
                for r in lang_raw:
                    r["consensus"] = "Single model (skipped consensus)"
                new_results.extend(lang_raw)
            else:
                # Count votes (case-insensitive)
                votes = {} # normalized_translation -> count
                for r in lang_raw:
                    norm = r["translation"].strip().lower()
                    votes[norm] = votes.get(norm, 0) + 1
                
                # Filter results that have consensus (2+ votes)
                consensus_norms = [norm for norm, count in votes.items() if count >= 2]
                
                if consensus_norms:
                    print(f"    Consensus reached for [{lang}]: {consensus_norms}")
                    for r in lang_raw:
                        norm = r["translation"].strip().lower()
                        if norm in consensus_norms:
                            # Add consensus info: count/total
                            count = votes[norm]
                            r["consensus"] = f"Consensus reached ({count}/{len(models)} models agreed)"
                        else:
                            r["consensus"] = "No consensus"
                    new_results.extend(lang_raw)
                else:
                    # Arbitration Phase
                    available_terms = list(set([r["translation"] for r in lang_raw if r["translation"]]))
                    print(f"    No consensus for [{lang}]. Candidates: {available_terms}")
                    print(f"    Starting Arbitration for [{lang}]...")
                    
                    arbitration_votes = []
                    with concurrent.futures.ThreadPoolExecutor(max_workers=len(models)) as executor:
                        future_to_model = {
                            executor.submit(_arbitrate_model, term, context, available_terms, model, arbitrator_prompt_template): model 
                            for model in models
                        }
                        for future in concurrent.futures.as_completed(future_to_model):
                            try:
                                vote = future.result()
                                if vote:
                                    arbitration_votes.append(vote)
                            except Exception as e:
                                print(f"Arbitration error: {e}")
                                
                    # Count arbitration votes
                    arb_counts = {}
                    for v in arbitration_votes:
                        norm = v.strip().lower()
                        arb_counts[norm] = arb_counts.get(norm, 0) + 1
                        
                    # Check for new consensus (simple majority or >= 2)
                    # Let's say we need at least 2 votes for the same thing to override
                    arb_consensus = [norm for norm, count in arb_counts.items() if count >= 2]
                    
                    if arb_consensus:
                        winner_norm = arb_consensus[0]
                        winner_text = [v for v in arbitration_votes if v.strip().lower() == winner_norm][0] # Get original casing
                        count = arb_counts[winner_norm]
                        print(f"    Arbitration successful! Winner: {winner_text} ({count} votes)")
                        
                        # Update all results for this lang to point to the winner? 
                        # Or just mark the winner? 
                        # Let's add a new result entry for the Arbitrated Winner or update existing ones.
                        # For simplicity, we mark the rows that match the winner as "Consensus reached (Arbitrated)"
                        # and ensure others are "No consensus".
                        
                        found_match = False
                        for r in lang_raw:
                            if r["translation"].strip().lower() == winner_norm:
                                r["consensus"] = f"Consensus reached (Arbitrated {count}/{len(models)})"
                                found_match = True
                            else:
                                r["consensus"] = "No consensus (Arbitration lost)"
                        
                        # If the winner wasn't in original raw results exactly (maybe slight variation returned by arbitrator?), 
                        # we might need to handle that. But generic instructions say "Select...". 
                        # Assuming models output one of the candidates.
                        
                        new_results.extend(lang_raw)
                    else:
                        print(f"    Arbitration failed. No clear winner.")
                        for r in lang_raw:
                            r["consensus"] = "No consensus (Arbitration failed)"
                        new_results.extend(lang_raw)

    # Merge new_results into results
    existing_map = {(r["term"], r["language"], r["winning_model"]): i for i, r in enumerate(results)}
    for res in new_results:
        key = (res["term"], res["language"], res["winning_model"])
        if key in existing_map:
            results[existing_map[key]] = res
        else:
            results.append(res)
            
    return results

def main():

    start_time = time.time()
    
    parser = argparse.ArgumentParser(description="Orchestrator for Multilingual CV Skill")
    parser.add_argument("--input-file", "--input_file", dest="input_file", help="Path to source CSV")
    parser.add_argument("--url", help="URL to scrape term from (overrides input_file)")
    parser.add_argument("--index-url", help="Index page URL to scrape multiple concepts from")
    parser.add_argument("--output-dir", "--output_dir", dest="output_dir", default="data", help="Directory for output CSV")
    parser.add_argument("--languages", default="fr,es,de", help="Comma-separated target languages")
    parser.add_argument("--models", default="gpt-oss:latest", help="Comma-separated LLM models to use")
    
    args = parser.parse_args()
    
    # Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    prompts_dir = os.path.join(base_dir, "prompts")
    prompts_dir = os.path.join(base_dir, "prompts")
    voter_prompt_template = load_prompt(os.path.join(prompts_dir, "voter_prompt.md"))
    arbitrator_prompt_template = load_prompt(os.path.join(prompts_dir, "arbitrator_prompt.md"))
    
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
    elif args.index_url:
        urls = scrape_index_page(args.index_url)
        if not urls:
            print("No URLs found in index page.")
            return
        
        # Scrape each URL found
        rows = []
        print(f"Processing {len(urls)} concepts from index...")
        for i, u in enumerate(urls):
            print(f"[{i+1}/{len(urls)}] Scraping {u}")
            try:
                t, c = scrape_url(u)
                rows.append({"term": t, "context": c})
                # Be searching friendly
                time.sleep(1) 
            except Exception as e:
                print(f"Skipping {u}: {e}")

    elif args.input_file:
        with open(args.input_file, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    else:
        print("Error: Must provide --url, --index-url, or --input-file")
        return
            
            
    results = process_terms(rows, languages, models, voter_prompt_template, arbitrator_prompt_template, output_csv_path)
    
    # Write Results
    fieldnames = ["term", "translation", "context", "language", "confidence", "winning_model", "consensus", "version"]
    for res in results:
        res["version"] = "0.1"
        if "consensus" not in res:
             res["consensus"] = "No consensus"
        
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
        # Use a dict to keep only ONE consensus winner per language
        lang_winners = {} 
        for res in results:
            if res.get("term") == last_term:
                lang = res.get("language")
                trans = res.get("translation")
                model = res.get("winning_model")
                consensus = res.get("consensus", "")
                
                # Only include in Croissant metadata if consensus was reached
                if lang and trans and ("Consensus reached" in consensus or "Single model" in consensus):
                    # Map to a single entry per language
                    if lang not in lang_winners:
                        lang_winners[lang] = {
                            "value": trans, # Use the first one found (they are semantically identical)
                            "lang": lang,
                            "model": model
                        }
        
        for lang_entry in lang_winners.values():
            name_list.append(lang_entry)
        
        # Serialize to JSON
        name_json = json.dumps(name_list)
        
        # Clean context for description (remove newlines, truncate if too long)
        clean_desc = last_context.replace("\n", " ").strip()
        if len(clean_desc) > 200:
             clean_desc = clean_desc[:197] + "..."
             
        cmd.extend(["--dataset-name", name_json])
        cmd.extend(["--description", clean_desc])
        cmd.extend(["--llm-model", args.models])
        
        # Calculate output filename
        # term without space and croissant, for example croissant_downburst.json
        safe_term = last_term.strip().replace(" ", "_").lower()
        output_filename = f"croissant_{safe_term}.json"
        cmd.extend(["--output-file", output_filename])

    if args.url:
        cmd.extend(["--source-url", args.url])
    elif args.input_file:
        cmd.extend(["--source-file", args.input_file])
        
    subprocess.run(cmd)
    
    elapsed_time = time.time() - start_time
    print(f"\nExecution finished in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
