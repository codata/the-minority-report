import os
import sys
import json
from fastmcp import FastMCP

# Ensure we can import orchestrator from the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

try:
    from orchestrator import scrape_url, process_terms, load_prompt
except ImportError:
    # Fallback if running from a different context
    from translation_skill.scripts.orchestrator import scrape_url, process_terms, load_prompt

mcp = FastMCP("Rosetta AI")

# Setup project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
OUTPUT_CSV_PATH = os.path.join(DATA_DIR, "final_translations.csv")

def _understand_and_translate_logic(term: str, context: str, languages: str = "fr,es,de", models: str = "gpt-oss:latest") -> str:
    """Helper function to perform translation logic."""
    voter_prompt_path = os.path.join(PROMPTS_DIR, "voter_prompt.md")
    voter_prompt_template = load_prompt(voter_prompt_path)
    
    rows = [{"term": term, "context": context}]
    lang_list = languages.split(",")
    model_list = models.split(",")
    
    results = process_terms(rows, lang_list, model_list, voter_prompt_template, OUTPUT_CSV_PATH)
    
    # Filter results for just this term
    term_results = [r for r in results if r["term"] == term]
    return json.dumps(term_results, indent=2)

@mcp.tool()
def understand_and_translate(term: str, context: str, languages: str = "fr,es,de", models: str = "gpt-oss:latest") -> str:
    """
    Translates a specialized technical term based on a conceptual context (Scope Note).
    
    Args:
        term: The technical term to translate.
        context: The Scope Note or definition of the term.
        languages: Comma-separated ISO codes (e.g., 'fr,es,de').
        models: Comma-separated Ollama models (e.g., 'gpt-oss:latest').
    """
    return _understand_and_translate_logic(term, context, languages, models)

@mcp.tool()
def open_page_and_translate(url: str, languages: str = "fr,es,de", models: str = "gpt-oss:latest") -> str:
    """
    Scrapes a term and its context from a URL (e.g., PreventionWeb) and translates it.
    
    Args:
        url: The URL to scrape.
        languages: Comma-separated ISO codes.
        models: Comma-separated Ollama models.
    """
    term, context = scrape_url(url)
    return _understand_and_translate_logic(term, context, languages, models)

if __name__ == "__main__":
    mcp.run()
