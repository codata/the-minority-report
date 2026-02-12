import csv
import json
import argparse
import os
import subprocess
import random
import datetime
import time
import re
import urllib.parse
import concurrent.futures
import sys
import functools
import threading

# Redirect all print calls to stderr to avoid breaking MCP stdio transport
print = functools.partial(print, file=sys.stderr)

# Hack: Fix OLLAMA_HOST if it contains commas (multi-host) before importing ollama lib
raw_ollama_host = os.environ.get('OLLAMA_HOST', '')
if ',' in raw_ollama_host:
    os.environ['OLLAMA_HOSTS_RAW'] = raw_ollama_host
    os.environ['OLLAMA_HOST'] = raw_ollama_host.split(',')[0].strip()

# --- Mock LLM Interface ---
from ollama import Client
import requests
from bs4 import BeautifulSoup
from ontoportal import OntoPortalClient

def generate_croissant_for_term(term_results, args, output_dir, data_file):
    """
    Generates a Croissant JSON-LD file for a single term's results.
    """
    if not term_results:
        return

    # Assuming all results are for the same term
    first_res = term_results[0]
    term = first_res.get("term", "Unknown")
    context = first_res.get("context", "")
    
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "croissant_generator.py")
    cmd = ["python3", script_path, "--output-dir", output_dir, "--data-file", data_file]
    
    # Build multilingual name list (Consensus only)
    name_list = [{"value": term, "lang": "en"}]
    
    # Filter for consensus
    lang_winners = {}
    for res in term_results:
        lang = res.get("language")
        trans = res.get("translation")
        consensus = res.get("consensus", "")
        # Use simple check
        if lang and trans and ("Consensus reached" in consensus or "Single model" in consensus):
             if lang not in lang_winners:
                 lang_winners[lang] = {
                     "value": trans,
                     "lang": lang,
                     "model": res.get("winning_model")
                 }
    
    for lang_entry in lang_winners.values():
        name_list.append(lang_entry)
        
    cmd.extend(["--dataset-name", json.dumps(name_list)])
    
    # Description
    clean_desc = context.replace("\n", " ").strip()
    if len(clean_desc) > 200:
         clean_desc = clean_desc[:197] + "..."
    cmd.extend(["--description", clean_desc])
    cmd.extend(["--llm-model", args.models])
    
    # HIPS Code
    hips_code = None
    if args.hips_code:
         hips_code = args.hips_code
    elif args.url and "hips/" in args.url:
         match = re.search(r"hips/([a-zA-Z0-9]+)", args.url)
         if match:
             hips_code = match.group(1).upper()
    
    # Fallback to result code
    if not hips_code:
        if first_res.get("code"):
            hips_code = first_res.get("code")
            
    if hips_code:
         cmd.extend(["--hips-code", hips_code])
         
    # Source
    if args.url:
        cmd.extend(["--source-url", args.url])
    elif args.input_file:
        cmd.extend(["--source-file", args.input_file])
    elif first_res.get("url"):
        cmd.extend(["--source-url", first_res.get("url")])

    # Output File
    safe_term = re.sub(r'[^\w\s-]', '', term.strip().lower())
    safe_term = re.sub(r'[-\s]+', '_', safe_term)
    output_filename = f"croissant_{safe_term}.json"
    cmd.extend(["--output-file", output_filename])
    
    # Run
    try:
        subprocess.run(cmd, check=False) # Don't crash if generator fails
    except Exception as e:
        print(f"Error running croissant generator: {e}")



# Parse hosts from environment (comma-separated)

# Parse hosts from environment (comma-separated)
# Order of precedence: OLLAMA_HOSTS > OLLAMA_HOSTS_RAW > OLLAMA_HOST
raw_hosts = os.environ.get('OLLAMA_HOSTS', os.environ.get('OLLAMA_HOSTS_RAW', os.environ.get('OLLAMA_HOST', 'http://10.147.18.253:11434')))
OLLAMA_HOSTS = [h.strip() for h in raw_hosts.split(',')]


import threading
from ontoportal import OntoPortalClient


import threading
from ontoportal import OntoPortalClient


import threading
from ontoportal import OntoPortalClient

class ModelRouter:
    def __init__(self, hosts):
        self.hosts = hosts
        self.lock = threading.Lock()
        # Initialize clients for each host
        self.clients = {}
        for h in hosts:
            try:
                self.clients[h] = Client(host=h, timeout=600)
            except Exception as e:
                print(f"[ModelRouter] Warning: Failed to init client for {h}: {e}")
        
        self.allocations = {} # model_name -> host_url

    def get_client(self, model_name):
        with self.lock:
            # If already allocated, return that client
            if model_name in self.allocations:
                host = self.allocations[model_name]
                return self.clients.get(host)
                
            # New model: Allocate to host with fewest assigned models
            # 1. Count current allocations per host
            host_counts = {h: 0 for h in self.hosts}
            for m, h in self.allocations.items():
                if h in host_counts:
                    host_counts[h] += 1
                    
            # 2. Pick host with min count
            # (Tie-break by order in list)
            best_host = min(host_counts, key=host_counts.get)
            
            self.allocations[model_name] = best_host
            print(f"[ModelRouter] assigning model '{model_name}' to host '{best_host}'")
            
            return self.clients.get(best_host)

# Global router instance - Eager instantiation to avoid race conditions in threads
_ROUTER = ModelRouter(OLLAMA_HOSTS)

def get_router():
    return _ROUTER

def mock_llm_call(prompt, model="gpt-oss:latest", is_json=True):
    """
    Calls the Ollama API using the OLLAMA_HOST environment variable.
    """
    try:
        router = get_router()
        client = router.get_client(model)
        
        if not client:
             print(f"Error: No client available for model {model}")
             return "{}"

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
    # Fix 1: Remove quotes after numbers (e.g. 0.96"})
    # Look for number followed immediately by quote then } or , or ]
    json_str = re.sub(r'(\d+(?:\.\d+)?)"\s*([,}\]])', r'\1\2', json_str)
    
    # Fix 2: Unescaped quotes inside strings? (Harder to do safely with regex)
    
    return json_str

# --- Main Logic ---

def load_prompt(path):
    with open(path, "r") as f:
        return f.read()

def get_google_sheet_csv_url(url):
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if not match:
        raise ValueError("Invalid Google Sheet URL")
    sheet_id = match.group(1)
    gid = "0"
    match_gid = re.search(r'[#&?]gid=([0-9]+)', url)
    if match_gid:
        gid = match_gid.group(1)
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"


def parse_ontoportal_url(url):
    """
    Check if URL is an OntoPortal URL and extract concept info.
    Returns (ontology, concept_id) or (None, None).
    """
    parsed = urllib.parse.urlparse(url)
    if not parsed.query:
        return None, None
        
    params = urllib.parse.parse_qs(parsed.query)
    concept_id = params.get('conceptid', [None])[0]
    
    # Try to extract ontology from path (e.g. /ontologies/CODE)
    ontology = None
    path_parts = parsed.path.split('/')
    if 'ontologies' in path_parts:
        try:
            idx = path_parts.index('ontologies')
            if idx + 1 < len(path_parts):
                ontology = path_parts[idx+1]
        except ValueError:
            pass
            
    return ontology, concept_id

def scrape_url(url, ontoportal_client=None):
    """
    Scrapes term and context from a URL.
    if ontoportal_client is provided, it tries to use it for OntoPortal URLs.
    """
    # OntoPortal Logic
    if ontoportal_client:
        ontology, concept_id = parse_ontoportal_url(url)
        if concept_id:
            print(f"Detected OntoPortal concept: {concept_id}")
            # Try to search/get details
            # We assume concept_id is the URI.
            # We use search because get_term_details needs the API ID url, which we might not have.
            try:
                results = ontoportal_client.search_term(concept_id, ontology=ontology)
                if results:
                    res = results[0]
                    term = res.get('prefLabel')
                    defs = res.get('definition', [])
                    context_text = defs[0] if isinstance(defs, list) and defs else str(defs)
                    if not context_text: context_text = "No definition found in OntoPortal."
                    
                    print(f"Resolved via API: {term}")
                    return term, context_text
            except Exception as e:
                print(f"OntoPortal search failed: {e}. Trying SPARQL fallback...")
                try:
                     sparql_res = ontoportal_client.resolve_uri_via_sparql(concept_id, ontology=ontology)
                     if sparql_res:
                         term = sparql_res.get('label')
                         context_text = sparql_res.get('definition', "No definition found via SPARQL.")
                         print(f"Resolved via SPARQL: {term}")
                         return term, context_text
                except Exception as sparql_e:
                     print(f"SPARQL fallback failed: {sparql_e}")
                
                 # Fallback to scraping

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
    print(f"Found {len(links)} unique concept URLs.")
    return list(links)

def load_index_cache(cache_path):
    if os.path.exists(cache_path):
        try:
            with open(cache_path, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_index_cache(cache_path, cache_data):
    try:
         with open(cache_path, "w") as f:
             json.dump(cache_data, f, indent=2)
    except Exception as e:
         print(f"Warning: Failed to save cache: {e}")

def get_hips_code_from_url(url):
    import re
    match = re.search(r"hips/([a-zA-Z0-9]+)", url)
    return match.group(1).upper() if match else None

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
            print(f"    [{model}] -> {lang}: {translation}")
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

def process_terms(rows, languages, models, voter_prompt_template, arbitrator_prompt_template, output_csv_path, args):
    """
    Processes a list of terms and returns translation results with consensus logic.
    A translation is only accepted if at least 2 models agree on it (case-insensitive).
    Output is generated incrementally, rewriting the file to ensure consensus consistency.
    """
    # 1. Load Existing Data
    # structure: term_data[term_lower][lang][model] = row_dict
    term_data = {} 
    
    filenames = ["term", "translation", "context", "language", "confidence", "winning_model", "consensus", "version", "code", "url"]

    if os.path.exists(output_csv_path):
        with open(output_csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                t = row.get("term", "").strip()
                l = row.get("language", "").strip()
                m = row.get("winning_model", "").strip()
                
                if not t: continue
                
                t_lower = t.lower()
                if t_lower not in term_data:
                    term_data[t_lower] = {}
                if l not in term_data[t_lower]:
                    term_data[t_lower][l] = {}
                
                term_data[t_lower][l][m] = row
                
    print(f"Loaded existing data for {len(term_data)} terms.")

    # 2. Process Input Rows
    for row_idx, row in enumerate(rows):
        term = row.get("term", "").strip()
        if not term: continue
        t_lower = term.lower()
        context = row.get("context", "")
        
        # Original metadata
        original_code = row.get("code")
        original_url = row.get("url")
        
        # Check which models we need to run for each language
        # We need to run a model if it's missing for ANY requested language? 
        # Or usually we run a model for ALL languages at once.
        # The `_query_model` function takes a list of languages.
        # So if Model A is missing for 'fr' but present for 'es', strictly speaking we might need to run it for 'fr'.
        # But `_query_model` returns all languages. 
        # Simpler approach: If Model A is missing for ANY requested language for this term, we run it for ALL languages (and overwrite/merge).
        
        models_to_run = []
        for m in models:
            # Check if this model has results for all languages for this term
            missing_any = False
            for lang in languages:
                if t_lower not in term_data or lang not in term_data[t_lower] or m not in term_data[t_lower][lang]:
                    missing_any = True
                    break
            
            if missing_any:
                models_to_run.append(m)
        
        if not models_to_run:
            print(f"Skipping '{term}' (all models present)")
            continue
            
        print(f"\nProcessing Term: {term}")
        print(f"  Backfilling models: {models_to_run}")

        # Execute missing models
        raw_results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(models_to_run)) as executor:
            future_to_model = {
                executor.submit(_query_model, term, context, languages, model, voter_prompt_template): model 
                for model in models_to_run
            }
            
            for future in concurrent.futures.as_completed(future_to_model):
                try:
                    data = future.result()
                    # Enrich
                    for d in data:
                        if original_code: d["code"] = original_code
                        if original_url: d["url"] = original_url
                    raw_results.extend(data)
                except Exception as exc:
                    print(f"Model generated exception: {exc}")

        # Now we have new results. We need to merge them with existing results to re-calculate consensus.
        # 1. Retrieve existing results for this term
        current_term_results = []
        if t_lower in term_data:
            for l_dict in term_data[t_lower].values():
                for m_row in l_dict.values():
                    # We only keep rows from models that we didn't just re-run
                    # (If we re-ran a model, we use the new result)
                    if m_row["winning_model"] not in models_to_run:
                         current_term_results.append(m_row)
        
        # 2. Add new results
        current_term_results.extend(raw_results)
        
        # 3. Recalculate Consensus per Language
        final_term_results = []
        
        for lang in languages:
            lang_raw = [r for r in current_term_results if r["language"] == lang]
            if not lang_raw: continue
            
            # Extract models present in this language batch
            present_models = set(r["winning_model"] for r in lang_raw)
            total_models_count = len(present_models) # Should be <= len(models)
            
            # Consensus Logic
            votes = {} 
            for r in lang_raw:
                norm = r["translation"].strip().lower()
                votes[norm] = votes.get(norm, 0) + 1
            
            consensus_norms = [norm for norm, count in votes.items() if count >= 2]
            
            consensus_msg = "No consensus"
            consensus_reached = False
            
            if len(models) == 1: # If global config is single model
                 consensus_msg = "Single model (skipped)"
                 consensus_reached = True
            elif consensus_norms:
                # Winner
                winner_norm = consensus_norms[0] # Pick first
                winner_text = next(r["translation"] for r in lang_raw if r["translation"].strip().lower() == winner_norm)
                count = votes[winner_norm]
                consensus_msg = f"Consensus reached ({count}/{total_models_count})"
                print(f"    [{lang}] Consensus: '{winner_text}'")
                
                # Mark rows
                for r in lang_raw:
                    if r["translation"].strip().lower() == winner_norm:
                        r["consensus"] = consensus_msg
                    else:
                        r["consensus"] = "No consensus"
            else:
                # Arbitration (Only if we have multiple contending votes)
                # If we just added new models and broken consensus, or still no consensus...
                # For simplicity in this backfill refactor, we skip complex re-arbitration trigger 
                # UNLESS we specifically want to implement it. 
                # Creating a new arbitration request here is complex because it's async.
                # Let's stick to simple voting for now, or reuse existing consensus message if valid?
                # No, we must update message.
                print(f"    [{lang}] No consensus among {total_models_count} models.")
                for r in lang_raw:
                     r["consensus"] = f"No consensus ({total_models_count} models)"
            
            final_term_results.extend(lang_raw)

        # 4. Update In-Memory Data
        if t_lower not in term_data: term_data[t_lower] = {}
        
        for res in final_term_results:
            l = res["language"]
            m = res["winning_model"]
            if l not in term_data[t_lower]: term_data[t_lower][l] = {}
            term_data[t_lower][l][m] = res
            
        # 5. Rewrite CSV (Atomic-ish)
        # We flatten term_data back to a list
        all_rows = []
        for t_dict in term_data.values():
            for l_dict in t_dict.values():
                for row_data in l_dict.values():
                    all_rows.append(row_data)
        
        try:
            with open(output_csv_path, "w") as f:
                writer = csv.DictWriter(f, fieldnames=filenames, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(all_rows)
            print(f"    Updated CSV. Total records: {len(all_rows)}")
            
            # Generate Croissant (Incremental)
            generate_croissant_for_term(final_term_results, args, args.output_dir, output_csv_path)
            
        except Exception as e:
            print(f"Error writing CSV: {e}")

    # Return final flat list
    flat_results = []
    for t_dict in term_data.values():
        for l_dict in t_dict.values():
            flat_results.extend(l_dict.values())
    return flat_results

def main():

    start_time = time.time()
    
    parser = argparse.ArgumentParser(description="Orchestrator for Multilingual CV Skill")
    parser.add_argument("--input-file", "--input_file", dest="input_file", help="Path to source CSV")
    parser.add_argument("--google-sheet", "--google_sheet", dest="google_sheet", help="Google Sheet URL to read terms from")
    parser.add_argument("--url", help="URL to scrape term from (overrides input_file)")
    parser.add_argument("--concept", help="Manual concept term (overrides input_file/url)")
    parser.add_argument("--context", help="Manual context/description for the concept")
    parser.add_argument("--index-url", help="Index page URL to scrape multiple concepts from (scrapes only, no translation)")
    parser.add_argument("--index-file", "--index_file", dest="index_file", help="Path to index cache JSON file to process")
    parser.add_argument("--output-dir", "--output_dir", dest="output_dir", default="data", help="Directory for output CSV")
    parser.add_argument("--languages", default="fr,es,de", help="Comma-separated target languages")
    parser.add_argument("--models", default="gpt-oss:latest", help="Comma-separated LLM models to use")
    parser.add_argument("--hips-code", "--hips_code", dest="hips_code", help="Manual HIPS code override")
    
    parser.add_argument("--ontoportal-api-key", default=os.environ.get("ONTOPORTAL_API_KEY"), help="API key for OntoPortal services (or set via ONTOPORTAL_API_KEY)")
    parser.add_argument("--ontoportal-url", default="http://ecoportal.lifewatch.eu:8080", help="Base URL for OntoPortal (default: EcoPortal)")

    args = parser.parse_args()
    
    # Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    prompts_dir = os.path.join(base_dir, "prompts")
    voter_prompt_template = load_prompt(os.path.join(prompts_dir, "voter_prompt.md"))
    arbitrator_prompt_template = load_prompt(os.path.join(prompts_dir, "arbitrator_prompt.md"))
    
    languages = args.languages.split(",")
    models = args.models.split(",")
    output_csv_path = os.path.join(args.output_dir, "final_translations.csv")
    
    # Initialize OntoPortal client if key provided
    ontoportal = None
    if args.ontoportal_api_key:
        ontoportal = OntoPortalClient(args.ontoportal_api_key, args.ontoportal_url)
        print(f"Enabled OntoPortal integration: {args.ontoportal_url}")
    
    # Read Source
    rows = []
    
    if args.concept:
        print(f"Processing manual concept: {args.concept}")
        rows = [{
            "term": args.concept,
            "context": args.context or f"Standard technical definition for {args.concept}.",
            "url": "manual-input"
        }]
    
    elif args.url:
        try:
            # Pass ontoportal client to scrape_url for smart resolution
            term, context_text = scrape_url(args.url, ontoportal_client=ontoportal)
            
            # --- OntoPortal Enrichment (if not already done via scrape_url smart path) ---
            # If we scaped via HTML, we might still want to enrich.
            # If we resolved via API, we already have the def, but maybe we want more?
            # logic inside scrape_url handles it.
            
            if ontoportal and "Official Definition" not in context_text:
                 # Only try to enrich if we didn't get a good one or if it was a plain scrap
                 op_def = ontoportal.get_definition(term)
                 if op_def:
                     print(f"  [OntoPortal] Found definition for '{term}'")
                     context_text += f"\n\nOfficial Definition (OntoPortal): {op_def}"

            rows.append({"term": term, "context": context_text})
        except Exception as e:
            print(f"Error scraping/resolving URL: {e}")
            return
            
    elif args.google_sheet:
        print(f"Reading from Google Sheet: {args.google_sheet}")
        csv_url = get_google_sheet_csv_url(args.google_sheet)
        try:
            # Download CSV
            resp = requests.get(csv_url)
            resp.raise_for_status()
            
            # Parse CSV
            # Decode content
            lines = resp.content.decode('utf-8').splitlines()
            reader = csv.DictReader(lines)
            
            # Map columns if needed (similar to sheet_reader logic)
            # We need standard 'term' and 'context' keys for processing
            raw_rows = list(reader)
            
            # Heuristic to find term/definition columns
            if raw_rows:
                keys = raw_rows[0].keys()
                term_col = next((c for c in keys if c.lower() in ['term', 'term_en', 'concept', 'label']), None)
                def_col = next((c for c in keys if c.lower() in ['definition', 'definition_en', 'context', 'description']), None)
                
                if term_col:
                     print(f"Mapped term column: {term_col}")
                     if def_col: print(f"Mapped context column: {def_col}")
                     
                     for r in raw_rows:
                         t = r.get(term_col, "").strip()
                         d = r.get(def_col, "").strip() if def_col else f"Standard definition for {t}"
                         if t:
                             rows.append({
                                 "term": t,
                                 "context": d,
                                 "url": args.google_sheet
                             })
                else:
                    print(f"Error: Could not identify term column in sheet. Found: {list(keys)}")
                    return
            
            print(f"Loaded {len(rows)} terms from Google Sheet.")
            
        except Exception as e:
            print(f"Error reading Google Sheet: {e}")
            return

    elif args.index_url:
        urls = scrape_index_page(args.index_url)
        if not urls:
            print("No URLs found in index page.")
            return
        
        # Load Cache
        cache_path = os.path.join(args.output_dir, "index_cache.json")
        index_cache = load_index_cache(cache_path)
        
        print(f"Processing {len(urls)} concepts from index...")
        
        cache_updated = False
        
        for i, u in enumerate(urls):
            # Check cache first
            if u in index_cache:
                print(f"[{i+1}/{len(urls)}] Cache exists for {u}")
                continue
                
            print(f"[{i+1}/{len(urls)}] Scraping {u}")
            try:
                t, c = scrape_url(u)
                code = get_hips_code_from_url(u)
                
                # Update Cache
                index_cache[u] = {
                    "term": t,
                    "context": c,
                    "code": code,
                    "url": u
                }
                cache_updated = True
                
                # Be searching friendly
                time.sleep(1) 
            except Exception as e:
                print(f"Skipping {u}: {e}")
                
        # Save cache if changed
        if cache_updated:
            save_index_cache(cache_path, index_cache)
            
        print(f"\nIndex creation complete. Saved to {cache_path}")
        print(f"Run translation with: --index-file {cache_path}")
        return

    elif args.index_file:
        print(f"Loading index file: {args.index_file}")
        with open(args.index_file, "r") as f:
            index_cache = json.load(f)
            # Convert values to list
            # We sort by term to be deterministic
            rows = list(index_cache.values())
            print(f"Loaded {len(rows)} terms from index file.")

    elif args.input_file:
        with open(args.input_file, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    else:
        print("Error: Must provide --url, --index-url, --index-file, or --input-file")
        return
            
            
    # args passed to process_terms
    results = process_terms(rows, languages, models, voter_prompt_template, arbitrator_prompt_template, output_csv_path, args)
    
    print(f"\nSuccess! All translations processed.")

    
    elapsed_time = time.time() - start_time
    print(f"\nExecution finished in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
