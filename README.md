# The Minority Report

> **Originally created for 2025 Hazard Information Profiles (HIPs) from United Nations Office for Disaster Risk Reduction.**
> This implementation is based on the novel "The Minority Report" by Philip K. Dick.

An agentic pipeline for generating high-quality multilingual technical translations and controlled vocabularies. The project uses a multi-model approach (Voter/Arbitrator architecture) to translate terms while preserving context and generating standard [Croissant](http://mlcommons.org/croissant/) metadata.

## Features

- **Multi-Model Orchestration**: Leverages `gpt-oss:latest`, `gemma3:27b`, and `deepseek-r1:14b` via Ollama.
- **Context-Aware Translation**: Uses "Scope Notes" to ensure technical accuracy.
- **Web Scraping**: Built-in support for extracting terms and definitions from sites like PreventionWeb.
- **Formal Provenance**: Every translation is linked to its source model in both CSV and Croissant metadata.
- **Arbitration Logic**: Automatically resolves disagreements between models by triggering a voting round.
- **Metrics Extraction**: Dynamically extracts quantifiable variables, indicators, and risk drivers from translated technical text using Chain-of-Thought prompting.
- **Semantic Croissant Catalog**: Automatically discovers and indexes all multi-lingual datasets, markdown articles, and metrics JSON objects into a single JSON-LD file.
- **Batch Processing**: Scrape entire indexes of terms and generate metadata in bulk.
- **Dockerized**: Easy deployment and execution without local environment headaches.

## ODRL Policy Governance

The translation pipeline is strictly governed by an Open Digital Rights Language (ODRL) policy (`ODRL/translation_pipeline_odrl.jsonld`). This policy mathematically enforces security, workflow, and quality constraints on the AI agents:

1. **Step 0 - Environment Verification**: The policy mandates that `OLLAMA_HOST`, `OLLAMA_MODEL`, and `OLLAMA_KEYWORDS_HOST` are present. If missing, the API throws an explicit ODRL Policy Violation.
2. **Step 1 - Ingest**: Explicit permission is granted to read from URLs or keyword strings.
3. **Step 2 & 3 - Keyword Extraction & Caching**: The system is permitted to use a secondary, specialized LLM to extract domain keywords, but holds a **duty** to archive them immediately to disk to preserve compute resources.
4. **Step 4 - Primary Translation**: Grants permission to translate the source text using the primary LLM grounded by the cached keywords.
5. **Step 5 & 6 - Validation & Retry**: Imposes a strict duty: the generated translation must be at least 75% of the length of the source text. If this validation fails, the policy mandates a consequence of retrying up to 3 times.
6. **Step 6.5 - Proofreading**: The translated text must be explicitly reviewed for language syntax, grammar, and natural flow by the model to correct any semantic or structural mistakes.
7. **Step 7 - Archiving**: The final validated translation and structural metadata must be saved following strict directory patterns.

The FastAPI service dynamically parses and enforces these ODRL rules at runtime.

## Installation

### Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- [Ollama](https://ollama.com/) (running on `http://10.147.18.253:11434` by default)

### Local Setup (Optional)
If you prefer running without Docker:
```bash
pip install -r requirements.txt
```

## Usage

### 🚀 Using Docker (Recommended)

1. **Build the Environment**:
   ```bash
   docker-compose build
   ```

2. **Index Scraping (Create Cache)**:
   Scrape an entire index page (e.g., PreventionWeb HIPS) to create a local cache of terms, URLs, and codes. This does **not** run translations yet.
   ```bash
   docker-compose run orchestrator --index-url https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/ --output-dir data
   ```
   *Output*: `data/index_cache.json`

3. **Run Translations (From Cache)**:
   Process the cached index file to translate all terms.
   ```bash
   docker-compose run orchestrator --index-file data/index_cache.json --languages fr,es,de --models gpt-oss:latest
   ```

   **With OntoPortal Enrichment (Optional):**
   Requires an API key (e.g., from [EcoPortal](http://ecoportal.lifewatch.eu)).
   ```bash
   export ONTOPORTAL_API_KEY="528c4e4a-5c3e-4798-a2e2-11d96761b8ce"
   
   docker-compose run -e ONTOPORTAL_API_KEY orchestrator \
     --index-file data/index_cache.json \
     --ontoportal-url "http://ecoportal.lifewatch.eu:8080"
   ```

4. **Single URL Mode**:
   Directly scrape and translate a single page.
   ```bash
   docker-compose run orchestrator --url https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/mh0103 --languages fr,es
   ```

   **OntoPortal-based Pages (e.g. AgroPortal):**
   The tool automatically detects OntoPortal URLs (containing `conceptid`) and uses the API to fetch the authoritative definition.
   ```bash
   export ONTOPORTAL_API_KEY="528c4e4a-5c3e-4798-a2e2-11d96761b8ce"

   docker-compose run -e ONTOPORTAL_API_KEY orchestrator \
     --url "https://agroportal.lirmm.fr/ontologies/NCBITAXON?p=classes&conceptid=http%3A%2F%2Fpurl.bioontology.org%2Fontology%2FSTY%2FT017" \
     --ontoportal-url "http://agroportal.lirmm.fr"
   ```

5. **Generate Batch Croissant Metadata**:
   Generate rich JSON-LD metadata for the entire dataset, enriching it with the HIPS codes and Source URLs from the index cache.
   ```bash
   docker-compose run python3 translation-skill/scripts/batch_croissant.py --input-file data/final_translations.csv --index-file data/index_cache.json --output-dir output/
   ```

6. **Extract Semantic Metrics**:
   Extract variables, indicators, and risk drivers from translated markdown files and store them in the CDIF directory structure. You can pass the `--language` flag to explicitly enforce the target language.
   ```bash
   python3 translation-skill/scripts/extract_metrics.py --hips-code GH0310 --language ru
   ```

7. **Generate Semantic Croissant**:
   Generates a central catalog (`semantic_croissant.json`) that recursively links all translated datasets, `.md` files, and `_metrics.json` records, providing explicit search directives for consumer agents.
   ```bash
   python3 translation-skill/scripts/generate_central_croissant.py
   ```

### 🐍 Using Python Directly

Ensure your `OLLAMA_HOST` is set:
```bash
export OLLAMA_HOST=http://10.147.18.253:11434
python3 translation-skill/scripts/orchestrator.py --url "YOUR_URL" --output_dir data
```

## MCP Server

The Minority Report can be run as a Model Context Protocol (MCP) server, allowing LLMs to use its translation and scraping tools directly. It provides:
- `understand_and_translate`: Translates a specialized term given its context (Scope Note).
- `open_page_and_translate`: Scrapes a term/context from a URL and translates it.

### How to Start the MCP Server

1. **Install Dependencies**:
   ```bash
   pip install fastmcp mcp --break-system-packages
   ```

2. **Run the Server**:
   ```bash
   python3 translation-skill/scripts/mcp_server.py
   ```

3. **Configure MCP Client**:
   Add the following to your MCP client configuration (e.g., Claude Desktop `mcp_config.json`):
   ```json
   {
     "mcpServers": {
       "minority-report": {
         "command": "python3",
         "args": ["/Users/vyacheslavtykhonov/projects/the-minority-report/translation-skill/scripts/mcp_server.py"],
         "env": {
           "OLLAMA_HOST": "http://10.147.18.253:11434"
         }
       }
     }
   }
   ```

### How to Use Minority Report MCP

Once configured, you can ask your LLM to perform complex technical translations.

**What to ask:**
- "Open the page https://www.preventionweb.net/... and translate the term into French and Spanish."
- "I have a technical term 'Digital Twin' used in the context of urban planning. Translate it into German and Dutch using The Minority Report."
- "Scrape the latest terminology from this URL and generate a multilingual controlled vocabulary entry."

**Tips:**
- **Provide Context**: The `understand_and_translate` tool works best when you provide a detailed "Scope Note" or definition.
- **Specify Models**: You can explicitly ask for certain models (e.g., `gemma3:27b`) if you need specific language nuances.
- **Batching**: While the MCP tools currenty handle one term at a time, you can ask the LLM to loop through a list of terms.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_HOST` | The URL of the Ollama API | `http://10.147.18.253:11434` |
| `SPACY_MODEL` | Path to the trained spaCy NER model for MCP server | `training/spacy_hips` |

## Configuration

### MCP Server
The MCP server uses a spaCy model for the `find_hazards` tool. 
- By default, it looks for the model at `training/spacy_hips`.
- You can override this by setting the `SPACY_MODEL` environment variable to the absolute path of your model.

```bash
export SPACY_MODEL=/path/to/your/custom/model
python3 translation-skill/scripts/mcp_server.py
```

## Project Structure
 
 - `translation-skill/scripts/`: Core logic for scraping, translation, and metadata generation.
 - `translation-skill/prompts/`: Markdown-based prompt templates for LLM agents.
 - `training/`: Model training scripts (spaCy NER and Transformers).
 - `tests/`: Verification scripts for the pipeline.
 - `data/`: Input and output CSV files.
 - `output/`: Generated Croissant metadata and SKOS vocabularies.
 - `agents.md`: Detailed documentation on agent architecture and prompts.

## Training Models

The project includes two training approaches for building custom models:

### spaCy NER Model (Recommended)


Train a lightweight Named Entity Recognition model to identify disaster terminology:

**Single-job training:**
```bash
# Install spaCy
pip install spacy

# Train the model (fast, ~1-2 minutes)
python3 training/train-spacy.py --data-dir output --n-iter 30 --test

# Model saved to: training/spacy_model/
```

**Parallel training (for multi-core systems):**
```bash
# Train 16 models in parallel
python3 training/train-spacy.py --data-dir output --n-jobs 16 --n-iter 30

# Monitor progress in another terminal
tail -f training/spacy_model/run_*.log

# Models saved to: training/spacy_model/run_0/, run_1/, ..., run_15/
```

**Advantages:**
- Fast training (1-2 minutes single-job, scales with cores for parallel)
- Small model size (~10MB per model)
- Works on CPU (GPU conflicts resolved via spawn multiprocessing)
- Production-ready
- Parallel training enables model ensembling or selection of best performer

### Transformers Fine-tuning (Advanced)

Fine-tune a Gemma model for translation tasks:

```bash
# Requires CUDA GPU
python3 training/train.py --data-dir output --model-name google/gemma-2-2b-it --max-steps 60
```

**Note:** This approach requires significant GPU resources and may take hours to train.

## Credits

- **Vyacheslav Tykhonov**: Project Lead & Architect.
- **GitHub**: [https://github.com/4tikhonov/the-minority-report](https://github.com/4tikhonov/the-minority-report)

## License
Distributed under the [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) license.
