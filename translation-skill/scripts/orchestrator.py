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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hips_html_parser import parse_html, get_extraction_pattern


# Redirect all print calls to stderr to avoid breaking MCP stdio transport
print = functools.partial(print, file=sys.stderr)

# Hack: Fix OLLAMA_HOST if it contains commas (multi-host) before importing ollama lib
# The ollama library crashes if OLLAMA_HOST has commas.
raw_ollama_host = os.environ.get('OLLAMA_HOST', '')
if ',' in raw_ollama_host:
    os.environ['OLLAMA_HOSTS_RAW'] = raw_ollama_host
    os.environ['OLLAMA_HOST'] = raw_ollama_host.split(',')[0].strip()



# --- Mock LLM Interface ---
from ollama import Client
import requests
from bs4 import BeautifulSoup


# Parse hosts from environment (comma-separated)

# Parse hosts from environment (comma-separated)
# Order of precedence: OLLAMA_HOSTS > OLLAMA_HOSTS_RAW > OLLAMA_HOST
raw_hosts = os.environ.get('OLLAMA_HOSTS', os.environ.get('OLLAMA_HOSTS_RAW', os.environ.get('OLLAMA_HOST', 'http://10.147.18.253:11434')))
OLLAMA_HOSTS = [h.strip() for h in raw_hosts.split(',')]


import threading
try:
    from ontoportal import OntoPortalClient
except ImportError:
    try:
        from translation_skill.scripts.ontoportal import OntoPortalClient
    except ImportError:
        print("Warning: ontoportal module not found. OntoPortal integration will be disabled.")
        OntoPortalClient = None

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
    Calls the Ollama API using the OLLAMA_HOST environment variable, or routes to the gemini CLI.
    """
    # Route to Gemini CLI if requested
    if "gemini" in model.lower():
        try:
            import subprocess
            
            # Map custom model names to supported Gemini API names (gemini-2.5-flash and gemini-2.5-pro are supported)
            actual_model = model
            if "gemini-2.5-pro" in model.lower():
                actual_model = "gemini-2.5-pro"
            else:
                actual_model = "gemini-2.5-flash"
                
            print(f"[Gemini CLI] Querying CLI with model: {actual_model} (mapped from {model})", file=sys.stderr)
            
            # Set trust workspace environment variable
            env = os.environ.copy()
            env["GEMINI_CLI_TRUST_WORKSPACE"] = "true"
            
            # Run the gemini CLI command. We use non-interactive (-p) and model (-m) flags, and pass --skip-trust.
            cmd = ["gemini", "--skip-trust", "-m", actual_model, "-p", prompt]
            
            # Execute command safely via subprocess without shell=True to avoid injection
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, env=env)
            response_text = result.stdout.strip()
            
            # Strip ANSI escape sequences (color codes) if present
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            response_text = ansi_escape.sub('', response_text)
            
            # Log response
            os.makedirs("logs", exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            with open(f"logs/prompt_{timestamp}.txt", "w") as f:
                f.write(prompt)
            with open(f"logs/response_{timestamp}.txt", "w") as f:
                f.write(f"Raw Object:\n{str(result)}\n\nExtracted Text:\n{response_text}")
                
            return response_text
        except FileNotFoundError:
            print(f"Error: 'gemini' CLI tool not found in PATH. Ensure it is installed.", file=sys.stderr)
            return "{}"
        except subprocess.CalledProcessError as e:
            print(f"Error calling Gemini CLI: command failed (exit code {e.returncode}). Stderr: {e.stderr}", file=sys.stderr)
            return "{}"
        except Exception as e:
            print(f"Error calling Gemini CLI: {e}", file=sys.stderr)
            return "{}"

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
            print(f"Description: {context_text}")
    # Return raw HTML content as third element
    return term, context_text, resp.text

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

def _query_model(term, context, languages, model, voter_prompt_template, method="standard", small_model="gemma4:e2b", keyword_prompt_template="", code=""):
    """Helper to query a single model and return parsed results."""
    if method == "rl" and keyword_prompt_template:
        cache_path = None
        if code and languages:
            base_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            cache_path = os.path.join(base_project_dir, "hips", code, "translations", languages[0], f"{code}_keywords.md")

        keywords = ""
        if cache_path and os.path.exists(cache_path):
            print(f"  [Keyword Extraction] Reading keywords from cache: {cache_path}")
            with open(cache_path, "r", encoding="utf-8") as f:
                keywords = f.read().strip()
        else:
            kw_prompt = keyword_prompt_template.replace("{{text}}", context)
            kw_prompt = kw_prompt.replace("{{term}}", term)
            print(f"  [Keyword Extraction] Using Model: {small_model}")
            keywords = mock_llm_call(kw_prompt, model=small_model, is_json=False).strip()
            if keywords and cache_path:
                os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                with open(cache_path, "w", encoding="utf-8") as f:
                    f.write(keywords)

        if keywords:
            print(f"    Keywords extracted: {keywords}")
            context += f"\n\nIdentified Domain Keywords: {keywords}"

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

def _query_model_longtext(text, language, model, longtext_prompt_template, method="standard", small_model="gemma4:e2b", keyword_prompt_template="", term="", code=""):
    """Helper to query a single model for long text translation (plaintext)."""
    if method == "rl" and keyword_prompt_template:
        cache_path = None
        if code and language:
            base_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            cache_path = os.path.join(base_project_dir, "hips", code, "translations", language, f"{code}_keywords.md")

        keywords = ""
        if cache_path and os.path.exists(cache_path):
            print(f"  [Keyword Extraction] Reading keywords from cache: {cache_path}")
            with open(cache_path, "r", encoding="utf-8") as f:
                keywords = f.read().strip()
        else:
            kw_prompt = keyword_prompt_template.replace("{{text}}", text)
            kw_prompt = kw_prompt.replace("{{term}}", term)
            print(f"  [Keyword Extraction] Using Model: {small_model}")
            keywords = mock_llm_call(kw_prompt, model=small_model, is_json=False).strip()
            if keywords and cache_path:
                os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                with open(cache_path, "w", encoding="utf-8") as f:
                    f.write(keywords)

        if keywords:
            print(f"    Keywords extracted: {keywords}")
            text += f"\n\nIdentified Domain Keywords: {keywords}"

    print(f"  [Longtext] Translating to {language} using Model: {model}")
    prompt = longtext_prompt_template.replace("{{target_language}}", language)
    prompt = prompt.replace("{{text}}", text)
    
    response_str = mock_llm_call(prompt, model=model).strip()
    
    # Extract the final corrected translation if the heading is present
    import re
    parts = re.split(r'(?i)\*?\*?(?:4\.\s*)?Corrected Translation:?\*?\*?', response_str)
    if len(parts) > 1:
        response_str = parts[-1].strip()
        
    # PROOFREADING STEP
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
        proofread_path = os.path.join(base_dir, "prompts", "proofread_prompt.md")
        if os.path.exists(proofread_path):
            with open(proofread_path, "r", encoding="utf-8") as pf:
                proofread_template = pf.read()
            print(f"  [Proofreading] Checking syntax and grammar for {language}...")
            p_prompt = proofread_template.replace("{{target_language}}", language).replace("{{text}}", response_str)
            proofread_str = mock_llm_call(p_prompt, model=model).strip()
            if proofread_str and len(proofread_str) > len(response_str) * 0.5: # Sanity check
                response_str = proofread_str
    except Exception as e:
        print(f"  [Proofreading Error] {e}")
        
    return response_str

        
def save_results_to_csv(results, output_csv_path):
    fieldnames = ["term", "translation", "context", "language", "confidence", "winning_model", "consensus", "version", "code", "url"]
    for res in results:
        res["version"] = "0.1"
        if "consensus" not in res:
             res["consensus"] = "No consensus"
             
    import tempfile
    temp_dir = os.path.dirname(output_csv_path) or "."
    if temp_dir:
        os.makedirs(temp_dir, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(dir=temp_dir, suffix=".tmp")
    try:
        with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(results)
        os.replace(temp_path, output_csv_path)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"Error saving results to CSV: {e}")

def process_terms(rows, languages, models, voter_prompt_template, arbitrator_prompt_template, longtext_prompt_template, output_csv_path, fields_to_translate=None, output_dir="data", method="standard", small_model="gemma4:e2b", keyword_prompt_template=""):
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
        
        # Original metadata to preserve
        original_code = row.get("code")
        original_url = row.get("url")
        
        # Field Translation Logic
        if fields_to_translate:
            source_file = row.get("source_file")
            code = row.get("code")
            if source_file and os.path.exists(source_file):
                print(f"  Extracting fields {fields_to_translate} from {source_file}...")
                try:
                    import json
                    
                    # Try to locate metadata.json
                    base_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                    metadata_path = os.path.join(base_project_dir, "hips", code, "output", "metadata.json") if code else None
                    if metadata_path and os.path.exists(metadata_path):
                        with open(metadata_path, "r") as f:
                            metadata = json.load(f)
                        pattern = get_extraction_pattern(metadata)
                        parsed_data = parse_html(source_file, pattern)
                        
                        primary_model = models[0]
                        for field in fields_to_translate:
                            field_text = parsed_data.get(field, parsed_data.get(f"{field}_text"))
                            if field_text and len(field_text.strip()) > 0:
                                for lang in languages:
                                    hips_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "hips", code)
                                    lang_dir = os.path.join(hips_dir, "translations", lang)
                                    os.makedirs(lang_dir, exist_ok=True)
                                    # For short fields or if it's text, we can just save it as text.
                                    # We use .md for all fields to support markdown formatting.
                                    out_file = os.path.join(lang_dir, f"{code}_{field}.md")
                                    input_len = len(field_text)
                                    if os.path.exists(out_file):
                                        with open(out_file, "r", encoding="utf-8") as f_out:
                                            existing_len = len(f_out.read())
                                        if existing_len >= 0.75 * input_len:
                                            print(f"    [{lang}] {field} already exists at {out_file} (size {existing_len}/{input_len}). Skipping.")
                                            continue
                                        else:
                                            print(f"    [{lang}] {field} exists but too small ({existing_len} < {0.75*input_len}). Re-translating.")
                                            
                                    max_retries = 3
                                    for attempt in range(max_retries):
                                        translated = _query_model_longtext(field_text, lang, primary_model, longtext_prompt_template, method, small_model, keyword_prompt_template, term, code)
                                        if translated:
                                            if len(translated) >= 0.75 * input_len:
                                                with open(out_file, "w", encoding="utf-8") as f_out:
                                                    f_out.write(translated)
                                                    print(f"    Saved {field} ({lang}) to {out_file} (size {len(translated)}/{input_len})")
                                                break
                                            else:
                                                print(f"    [{lang}] {field} translation failed size check ({len(translated)} < {0.75*input_len}). Attempt {attempt+1}/{max_retries}.")
                                                if attempt == max_retries - 1:
                                                    print(f"    [{lang}] {field} reached max retries. Not saving.")
                    else:
                        print(f"    Metadata not found at {metadata_path}. Skipping field translation.")
                except Exception as e:
                    print(f"    Error translating fields: {e}")
            else:
                print(f"  Source file '{source_file}' not found. Skipping field translation.")
        
        # Execute model queries in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(models)) as executor:
            future_to_model = {
                executor.submit(_query_model, term, context, languages, model, voter_prompt_template, method, small_model, keyword_prompt_template, original_code): model 
                for model in models
            }
            
            for future in concurrent.futures.as_completed(future_to_model):
                try:
                    data = future.result()
                    # Enrich results with original metadata
                    for d in data:
                        if original_code: d["code"] = original_code
                        if original_url: d["url"] = original_url
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
                    # Find the actual text for the consensus norm
                    consensus_text = next(r["translation"] for r in lang_raw if r["translation"].strip().lower() in consensus_norms)
                    print(f"    Consensus reached for [{lang}]: '{consensus_text}'")
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
                        
                        found_match = False
                        for r in lang_raw:
                            if r["translation"].strip().lower() == winner_norm:
                                r["consensus"] = f"Consensus reached (Arbitrated {count}/{len(models)})"
                                found_match = True
                            else:
                                r["consensus"] = "No consensus (Arbitration lost)"
                        
                        new_results.extend(lang_raw)
                    else:
                        print(f"    Arbitration failed. No clear winner.")
                        for r in lang_raw:
                            r["consensus"] = "No consensus (Arbitration failed)"
                        new_results.extend(lang_raw)
                        
        # Save incremental results to CSV at the end of each term's processing
        merged_results = list(results)
        existing_map = {(r["term"], r["language"], r["winning_model"]): i for i, r in enumerate(merged_results)}
        for res in new_results:
            key = (res["term"], res["language"], res["winning_model"])
            if key in existing_map:
                merged_results[existing_map[key]] = res
            else:
                merged_results.append(res)
        save_results_to_csv(merged_results, output_csv_path)

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
    parser.add_argument("--concept", help="Manual concept term (overrides input_file/url)")
    parser.add_argument("--context", help="Manual context/description for the concept")
    parser.add_argument("--index-url", help="Index page URL to scrape multiple concepts from (scrapes only, no translation)")
    parser.add_argument("--index-file", "--index_file", dest="index_file", help="Path to index cache JSON file to process")
    parser.add_argument("--output-dir", "--output_dir", dest="output_dir", default="data", help="Directory for output CSV")
    parser.add_argument("--languages", default="fr,es,de", help="Comma-separated target languages")
    parser.add_argument("--models", default="gpt-oss:latest", help="Comma-separated LLM models to use")
    parser.add_argument("--hips-code", "--hips_code", dest="hips_code", help="Manual HIPS code override")
    parser.add_argument("--fields", default="", help="Comma-separated list of fields to translate (e.g., title,summary,article,fulltext)")
    parser.add_argument("--method", default="standard", choices=["standard", "rl"], help="Translation method to use (standard or rl)")
    parser.add_argument("--small-model", default="gemma4:e2b", help="Small model to use for keyword extraction in RL method")
    
    parser.add_argument("--ontoportal-api-key", default=os.environ.get("ONTOPORTAL_API_KEY"), help="API key for OntoPortal services (or set via ONTOPORTAL_API_KEY)")
    parser.add_argument("--ontoportal-url", default="http://ecoportal.lifewatch.eu:8080", help="Base URL for OntoPortal (default: EcoPortal)")

    args = parser.parse_args()
    
    # Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    prompts_dir = os.path.join(base_dir, "prompts")
    voter_prompt_template = load_prompt(os.path.join(prompts_dir, "voter_prompt.md"))
    arbitrator_prompt_template = load_prompt(os.path.join(prompts_dir, "arbitrator_prompt.md"))
    longtext_prompt_template = load_prompt(os.path.join(prompts_dir, "longtext_prompt.md"))
    keyword_prompt_template = ""
    if args.method == "rl":
        kw_prompt_path = os.path.join(prompts_dir, "keyword_extraction_prompt.md")
        if os.path.exists(kw_prompt_path):
            keyword_prompt_template = load_prompt(kw_prompt_path)
        else:
            print(f"Warning: keyword extraction prompt not found at {kw_prompt_path}")
    
    languages = args.languages.split(",")
    models = args.models.split(",")
    fields_to_translate = [f.strip() for f in args.fields.split(",")] if args.fields else []
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
            term, context_text, raw_html = scrape_url(args.url, ontoportal_client=ontoportal)
            code = get_hips_code_from_url(args.url)
            
            # Save raw HTML to distribution folder for later reference
            distribution_dir = os.path.join(args.output_dir, "distribution")
            os.makedirs(distribution_dir, exist_ok=True)
            html_path = os.path.join(distribution_dir, f"{code}_{term.replace(' ', '_')}.html")
            try:
                with open(html_path, "w", encoding="utf-8") as f_html:
                    f_html.write(raw_html)
            except Exception as e:
                print(f"Warning: failed to save raw HTML for {term}: {e}")
            
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

            rows.append({
                "term": term, 
                "context": context_text,
                "code": code,
                "url": args.url,
                "source_file": html_path
            })
        except Exception as e:
            print(f"Error scraping/resolving URL: {e}")
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
                t, c, raw_html = scrape_url(u)
                code = get_hips_code_from_url(u)
                
                # Save raw HTML to distribution folder
                distribution_dir = os.path.join(args.output_dir, "distribution")
                os.makedirs(distribution_dir, exist_ok=True)
                html_path = os.path.join(distribution_dir, f"{code}_{t.replace(' ', '_')}.html")
                try:
                    with open(html_path, "w", encoding="utf-8") as f_html:
                        f_html.write(raw_html)
                except Exception as e:
                    print(f"Warning: failed to save raw HTML for {t}: {e}")
                
                # Update Cache
                index_cache[u] = {
                    "term": t,
                    "context": c,
                    "code": code,
                    "url": u,
                    "source_file": html_path
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
            
    results = process_terms(rows, languages, models, voter_prompt_template, arbitrator_prompt_template, longtext_prompt_template, output_csv_path, fields_to_translate, args.output_dir, args.method, args.small_model, keyword_prompt_template)
    
    # Write Results
    save_results_to_csv(results, output_csv_path)
        
    print(f"\nSuccess! Translations written to {output_csv_path}")
    
    # 3. Serialize (Croissant)
    print("Generating Croissant Metadata...")
    # call croissant_generator.py
    # We assume it's in the same scripts/ dir
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "croissant_generator.py")
    
    cmd = ["python3", script_path, "--data-file", output_csv_path, "--output-dir", "output/", "--source-file", os.path.join(args.output_dir, "distribution"), "--root-folder", ".", "--longtext-model", models[0]]
    
    # Check if we have a single term (URL mode or single row CSV) to name the dataset specifically
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

        # Extract HIPS code if present in URL
        # For cache mode, we might want to prioritize the code from the cache over regex from current URL args
        hips_code = None
        if args.hips_code:
             hips_code = args.hips_code
        elif args.url and "hips/" in args.url:
             match = re.search(r"hips/([a-zA-Z0-9]+)", args.url)
             if match:
                 hips_code = match.group(1).upper()
        # Fallback: check if the last term has a code in results
        if not hips_code and len(results) > 0:
             # Find result for last term
             last_res = next((r for r in results if r.get("term") == last_term), None)
             if last_res and last_res.get("code"):
                 hips_code = last_res.get("code")

        # Sync to individual hips folder if it exists for ALL processed codes
        print("Syncing generated metadata to individual HIPS folders...")
        
        # Load index cache for fallback lookups
        fallback_cache = {}
        cache_path = os.path.join(args.output_dir, "index_cache.json")
        if os.path.isfile(cache_path):
            with open(cache_path, "r") as f:
                c_data = json.load(f)
                for v in c_data.values():
                    if v.get("term") and v.get("code"):
                        fallback_cache[v["term"]] = v["code"]

        # Group results by hips_code
        grouped_results = {}
        for r in results:
            c = r.get("code")
            if not c:
                c = fallback_cache.get(r.get("term"))
                if c:
                    r["code"] = c  # Update it in the result so it saves correctly
            if c:
                if c not in grouped_results:
                    grouped_results[c] = []
                grouped_results[c].append(r)
                
        for h_code, h_results in grouped_results.items():
             hips_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hips", h_code)
             if os.path.isdir(hips_dir):
                 # 1. Update individual CSV
                 ind_csv = os.path.join(hips_dir, "data", "final_translations.csv")
                 os.makedirs(os.path.dirname(ind_csv), exist_ok=True)
                 with open(ind_csv, "w", newline="") as f:
                     fieldnames = ["term", "translation", "context", "language", "confidence", "winning_model", "consensus", "version", "code", "url"]
                     writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                     writer.writeheader()
                     for r in h_results:
                         writer.writerow(r)
                             
                 # 2. Run generator for individual folder
                 ind_cmd = [
                     "python3", script_path, 
                     "--data-file", ind_csv, 
                     "--output-dir", os.path.join(hips_dir, "output"), 
                     "--source-file", os.path.join(hips_dir, "data", "distribution"), 
                     "--hips-code", h_code, 
                     "--root-folder", ".",
                     "--longtext-model", models[0]
                 ]
                 subprocess.run(ind_cmd, capture_output=True)
        # term without space and croissant, for example croissant_downburst.json
        safe_term = re.sub(r'[^\w\s-]', '', last_term.strip().lower())
        safe_term = re.sub(r'[-\s]+', '_', safe_term)
        output_filename = f"croissant_{safe_term}.json"
        cmd.extend(["--output-file", output_filename])

    if args.url:
        cmd.extend(["--source-url", args.url])
    elif args.input_file:
        cmd.extend(["--source-file", args.input_file])
    # Also pass URL from last result if available and not passed args.url
    elif len(rows) > 0:
         # Try to find URL for last term
         last_res = next((r for r in results if r.get("term") == last_term), None)
         if last_res and last_res.get("url"):
              cmd.extend(["--source-url", last_res.get("url")])

        
    subprocess.run(cmd)
    
    elapsed_time = time.time() - start_time
    print(f"\nExecution finished in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
