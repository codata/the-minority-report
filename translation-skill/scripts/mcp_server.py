import os
import sys
import json
from fastmcp import FastMCP
import spacy

# Ensure we can import orchestrator from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

try:
    from orchestrator import scrape_url, process_terms, load_prompt
except ImportError:
    # Fallback if running from a different context
    from translation_skill.scripts.orchestrator import scrape_url, process_terms, load_prompt

mcp = FastMCP("Minority Report")

# Setup project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
OUTPUT_CSV_PATH = os.path.join(DATA_DIR, "final_translations.csv")
MODEL_PATH = os.environ.get("SPACY_MODEL", os.path.join(os.path.dirname(BASE_DIR), "training", "spacy_hips"))
NLP_MODEL = None

def _load_model():
    """Lazy load the spaCy model."""
    global NLP_MODEL
    if NLP_MODEL is None:
        try:
            print(f"Loading spaCy model from {MODEL_PATH}...")
            NLP_MODEL = spacy.load(MODEL_PATH)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise RuntimeError(f"Failed to load spaCy model from {MODEL_PATH}. Ensure it is trained.")
    return NLP_MODEL

def _understand_and_translate_logic(term: str, context: str, languages: str = "fr,es,de", models: str = "gpt-oss:latest") -> str:
    """Helper function to perform translation logic."""
    voter_prompt_path = os.path.join(PROMPTS_DIR, "voter_prompt.md")
    voter_prompt_template = load_prompt(voter_prompt_path)
    
    arbitrator_prompt_path = os.path.join(PROMPTS_DIR, "arbitrator_prompt.md")
    arbitrator_prompt_template = load_prompt(arbitrator_prompt_path)
    
    longtext_prompt_path = os.path.join(PROMPTS_DIR, "longtext_prompt.md")
    longtext_prompt_template = load_prompt(longtext_prompt_path)
    
    rows = [{"term": term, "context": context}]
    lang_list = [l.strip() for l in languages.split(",")]
    model_list = [m.strip() for m in models.split(",")]
    
    # if len(model_list) < 2:
    #     return json.dumps({"error": "Consensus logic requires at least 2 models. Please specify multiple models separated by commas."}, indent=2)
    
    
    results = process_terms(rows, lang_list, model_list, voter_prompt_template, arbitrator_prompt_template, longtext_prompt_template, OUTPUT_CSV_PATH)
    
    # Filter results for just this term
    term_results = [r for r in results if r["term"] == term]
    
    if not term_results:
        return json.dumps({"info": "No consensus reached between models for this term. Try adding more models or checking the context."}, indent=2)
        
    return json.dumps(term_results, indent=2)

@mcp.tool()
def understand_and_translate(term: str, context: str, languages: str = "fr,es,de", models: str = "gpt-oss:latest") -> str:
    """
    Translates a specialized technical term based on a conceptual context (Scope Note).
    
    Args:
        term: The technical term to translate.
        context: The Scope Note or definition of the term.
        languages: Comma-separated ISO codes (e.g., 'fr,es,de').
        models: Comma-separated Ollama models. At least 2 are required for consensus.
    """
    return _understand_and_translate_logic(term, context, languages, models)

@mcp.tool()
def open_page_and_translate(url: str, languages: str = "fr,es,de", models: str = "gpt-oss:latest") -> str:
    """
    Scrapes a term and its context from a URL (e.g., PreventionWeb) and translates it.
    
    Args:
        url: The URL to scrape.
        languages: Comma-separated ISO codes.
        models: Comma-separated Ollama models. At least 2 are required for consensus.
    """
    term, context = scrape_url(url)
    return _understand_and_translate_logic(term, context, languages, models)

def _find_hazards_logic(query: str) -> str:
    """Helper function to perform hazard extraction logic."""
    try:
        nlp = _load_model()
        doc = nlp(query)
        
        hazards = []
        for ent in doc.ents:
            hazards.append({
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char
            })
            
        return json.dumps(hazards, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})

@mcp.tool()
def find_hazards(query: str) -> str:
    """
    Analyzes a text query to identify disaster risk terminology and HIPS codes using a trained NER model.
    
    Args:
        query: The text to analyze for hazards.
    """
    return _find_hazards_logic(query)

if __name__ == "__main__":
    mcp.run()
