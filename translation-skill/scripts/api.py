import os
import sys
import json
import csv
import re
import io
from typing import List, Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, AnyHttpUrl

# Adjust Python path to allow imports from this folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)

# Mock fastmcp and mcp if not installed to prevent import errors
try:
    import fastmcp
except ImportError:
    from unittest.mock import MagicMock
    sys.modules['fastmcp'] = MagicMock()
try:
    import mcp
except ImportError:
    from unittest.mock import MagicMock
    sys.modules['mcp'] = MagicMock()

try:
    from orchestrator import scrape_url, process_terms, load_prompt, OntoPortalClient
    from mcp_server import _understand_and_translate_logic, _find_hazards_logic
    from croissant_generator import generate_croissant_metadata
except ImportError:
    # Fallback paths
    from translation_skill.scripts.orchestrator import scrape_url, process_terms, load_prompt, OntoPortalClient
    from translation_skill.scripts.mcp_server import _understand_and_translate_logic, _find_hazards_logic
    from translation_skill.scripts.croissant_generator import generate_croissant_metadata

app = FastAPI(
    title="Minority Report API",
    description="FastAPI service for disaster hazard term mapping and multilingual controlled vocabularies.",
    version="1.0.0"
)

# Enable CORS for localhost and standard developer interfaces
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Standard Paths
BASE_DIR = os.path.dirname(SCRIPT_DIR)
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
OUTPUT_CSV_PATH = os.path.join(DATA_DIR, "final_translations.csv")
HTML_PATH = os.path.join(SCRIPT_DIR, "index.html")

# Schemas
class TranslateRequest(BaseModel):
    term: str
    context: str
    languages: str = "fr,es,de"
    models: str = "gpt-oss:latest"

class ScrapeTranslateRequest(BaseModel):
    url: str
    languages: str = "fr,es,de"
    models: str = "gpt-oss:latest"

class HazardRequest(BaseModel):
    query: str

# Endpoints
@app.get("/", response_class=HTMLResponse)
def get_frontend():
    """Serves the premium single-page web application frontend."""
    if os.path.exists(HTML_PATH):
        with open(HTML_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Minority Report Frontend UI file not found.</h1>"

@app.post("/api/translate")
def translate_term(req: TranslateRequest):
    """
    Translates a single technical term based on conceptual context (Scope Note).
    Executes the multi-model Voter/Arbitrator consensus flow.
    """
    if not req.term.strip():
        raise HTTPException(status_code=400, detail="Term cannot be empty.")
    if not req.context.strip():
        raise HTTPException(status_code=400, detail="Context cannot be empty.")
    
    try:
        result_json_str = _understand_and_translate_logic(
            term=req.term.strip(),
            context=req.context.strip(),
            languages=req.languages.strip(),
            models=req.models.strip()
        )
        return json.loads(result_json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation pipeline error: {str(e)}")

@app.post("/api/scrape-translate")
def scrape_and_translate(req: ScrapeTranslateRequest):
    """
    Scrapes a target term and context from a source URL (e.g. PreventionWeb HIPS, EcoPortal)
    and executes the multi-model Voter/Arbitrator translation consensus flow.
    """
    url_str = req.url.strip()
    if not url_str.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="Invalid URL format. Must start with http or https.")
        
    try:
        # Initialize optional OntoPortal client if credentials exist in env
        ontoportal_api_key = os.environ.get("ONTOPORTAL_API_KEY")
        ontoportal_url = os.environ.get("ONTOPORTAL_URL", "http://ecoportal.lifewatch.eu:8080")
        ontoportal = None
        if ontoportal_api_key:
            ontoportal = OntoPortalClient(ontoportal_api_key, ontoportal_url)
            
        # Scrape
        term, context = scrape_url(url_str, ontoportal_client=ontoportal)
        
        if not term or term == "Unknown Term":
            raise ValueError("Failed to extract term from the target URL.")
            
        # Translate
        result_json_str = _understand_and_translate_logic(
            term=term,
            context=context,
            languages=req.languages.strip(),
            models=req.models.strip()
        )
        
        return {
            "term": term,
            "context": context,
            "results": json.loads(result_json_str)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scrape-Translate pipeline error: {str(e)}")

@app.post("/api/find-hazards")
def find_hazards(req: HazardRequest):
    """
    Analyzes raw text query using the trained spaCy NER model to identify disaster risk terminology.
    """
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query text cannot be empty.")
        
    try:
        result_json_str = _find_hazards_logic(req.query.strip())
        return json.loads(result_json_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NER model execution error: {str(e)}")

@app.post("/api/translate-csv")
async def translate_csv_batch(
    file: UploadFile = File(...),
    languages: str = Form("fr,es,de"),
    models: str = Form("gpt-oss:latest")
):
    """
    Accepts an uploaded CSV file containing terms & contexts, processes the batch translation pipeline,
    and returns consensus translation metadata.
    """
    # 1. Enforce size limit check (Max 10MB) to protect against DoS
    max_size = 10 * 1024 * 1024
    content = await file.read(max_size + 1)
    if len(content) > max_size:
        raise HTTPException(status_code=400, detail="Uploaded file size exceeds 10MB limit.")
        
    # Seek to start
    await file.seek(0)
    file_bytes = await file.read()
    
    try:
        decoded = file_bytes.decode('utf-8')
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Invalid file encoding. File must be UTF-8 encoded CSV.")
        
    # Parse CSV in-memory safely (avoid saving uploaded files in web-root)
    csv_file = io.StringIO(decoded)
    reader = csv.DictReader(csv_file)
    
    if not reader.fieldnames:
        raise HTTPException(status_code=400, detail="Empty CSV file or invalid header.")
        
    headers = [h.strip().lower() for h in reader.fieldnames]
    if "term" not in headers or "context" not in headers:
        raise HTTPException(status_code=400, detail="CSV must contain both 'term' and 'context' columns.")
        
    # Read rows
    rows = []
    for row in reader:
        # Standardize keys to lowercase
        normalized_row = {k.strip().lower(): v for k, v in row.items() if k}
        rows.append({
            "term": normalized_row.get("term", ""),
            "context": normalized_row.get("context", ""),
            "code": normalized_row.get("code", ""),
            "url": normalized_row.get("url", "")
        })
        
    if not rows:
        raise HTTPException(status_code=400, detail="CSV does not contain any valid translation rows.")
        
    try:
        voter_prompt_path = os.path.join(PROMPTS_DIR, "voter_prompt.md")
        voter_prompt_template = load_prompt(voter_prompt_path)
        
        arbitrator_prompt_path = os.path.join(PROMPTS_DIR, "arbitrator_prompt.md")
        arbitrator_prompt_template = load_prompt(arbitrator_prompt_path)
        
        lang_list = [l.strip() for l in languages.split(",")]
        model_list = [m.strip() for m in models.split(",")]
        
        results = process_terms(
            rows=rows,
            languages=lang_list,
            models=model_list,
            voter_prompt_template=voter_prompt_template,
            arbitrator_prompt_template=arbitrator_prompt_template,
            output_csv_path=OUTPUT_CSV_PATH
        )
        
        # Write results back to CSV
        fieldnames = ["term", "translation", "context", "language", "confidence", "winning_model", "consensus", "version", "code", "url"]
        for res in results:
            res["version"] = "0.1"
            if "consensus" not in res:
                res["consensus"] = "No consensus"
                
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(OUTPUT_CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(results)
            
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch CSV translation error: {str(e)}")

@app.get("/api/translations")
def get_all_translations():
    """Returns all translation records stored in final_translations.csv."""
    if not os.path.exists(OUTPUT_CSV_PATH):
        return []
        
    try:
        results = []
        with open(OUTPUT_CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                results.append(row)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read database: {str(e)}")

def _get_croissant_metadata_logic(term: str) -> dict:
    """Helper to load translation records for a term and generate Croissant metadata on-the-fly."""
    if not os.path.exists(OUTPUT_CSV_PATH):
        raise HTTPException(status_code=404, detail="Translations database does not exist yet. Run a translation first.")
        
    term_rows = []
    with open(OUTPUT_CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("term", "").strip().lower() == term.strip().lower():
                term_rows.append(row)
                
    if not term_rows:
        raise HTTPException(status_code=404, detail=f"No translation records found for term '{term}'.")
        
    # Extract metadata properties from first match
    first_match = term_rows[0]
    description = first_match.get("context", f"Controlled vocabulary entry for {term}")
    source_url = first_match.get("url")
    hips_code = first_match.get("code")
    
    # Determine models
    models = list(set([r.get("winning_model") for r in term_rows if r.get("winning_model")]))
    models_str = ",".join(models) if models else "gpt-oss:latest"
    
    # Construct name_list schema mapping
    name_list = [{"value": term, "lang": "en"}]
    for r in term_rows:
        lang = r.get("language")
        trans = r.get("translation")
        model = r.get("winning_model")
        consensus = r.get("consensus", "")
        if lang and trans and ("Consensus reached" in consensus or "Single model" in consensus):
            name_list.append({
                "value": trans,
                "lang": lang,
                "model": model
            })
            
    dataset_name_json = json.dumps(name_list)
    
    try:
        metadata = generate_croissant_metadata(
            dataset_name=dataset_name_json,
            description=description,
            file_path=OUTPUT_CSV_PATH,
            num_records=len(term_rows),
            source_url=source_url,
            llm_model=models_str,
            hips_code=hips_code
        )
        return metadata
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Croissant generation error: {str(e)}")

@app.get("/api/croissant/{term}")
def get_croissant_metadata(term: str):
    """Generates and returns Croissant JSON-LD metadata for the requested term."""
    return _get_croissant_metadata_logic(term)

@app.get("/api/croissant/{term}/download")
def download_croissant_metadata(term: str):
    """Generates and serves the Croissant JSON-LD file for download."""
    # Defend against path injection (defense-in-depth)
    safe_term = re.sub(r'[^\w\s-]', '', term.strip().lower())
    safe_term = re.sub(r'[-\s]+', '_', safe_term)
    filename = f"croissant_{safe_term}.json"
    filename = os.path.basename(filename) # Strip traversal paths
    
    metadata = _get_croissant_metadata_logic(term)
    
    # Convert to json bytes
    json_bytes = json.dumps(metadata, indent=2).encode("utf-8")
    
    return Response(
        content=json_bytes,
        media_type="application/ld+json",
        headers={
            "Content-Disposition": f"attachment; filename={filename}",
            "X-Content-Type-Options": "nosniff"
        }
    )

if __name__ == "__main__":
    # In production, bind to 0.0.0.0, but follow the Secure Coding rule:
    # "Servers MUST listen on localhost or 127.0.0.1 when testing."
    # We retrieve config from environment or default to 127.0.0.1 for safety
    host = os.environ.get("API_HOST", "127.0.0.1")
    port = int(os.environ.get("API_PORT", "8000"))
    
    print(f"Starting server at http://{host}:{port}")
    uvicorn.run("api:app", host=host, port=port, reload=True)
