# The Minority Report

> This implementation is based on the novel "The Minority Report" by Philip K. Dick.

An agentic pipeline for generating high-quality multilingual technical translations and controlled vocabularies. The project uses a multi-model approach (Voter/Arbitrator architecture) to translate terms while preserving context and generating standard [Croissant](http://mlcommons.org/croissant/) metadata.

## Features

- **Multi-Model Orchestration**: Leverages `gpt-oss:latest`, `gemma3:27b`, and `deepseek-r1:14b` via Ollama.
- **Context-Aware Translation**: Uses "Scope Notes" to ensure technical accuracy.
- **Web Scraping**: Built-in support for extracting terms and definitions from sites like PreventionWeb.
- **Formal Provenance**: Every translation is linked to its source model in both CSV and Croissant metadata.
- **Arbitration Logic**: Automatically resolves disagreements between models by triggering a voting round.
- **Batch Processing**: Scrape entire indexes of terms and generate metadata in bulk.
- **Dockerized**: Easy deployment and execution without local environment headaches.

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

4. **Single URL Mode**:
   Directly scrape and translate a single page.
   ```bash
   docker-compose run orchestrator --url https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/mh0103 --languages fr,es
   ```

5. **Generate Batch Croissant Metadata**:
   Generate rich JSON-LD metadata for the entire dataset, enriching it with the HIPS codes and Source URLs from the index cache.
   ```bash
   docker-compose run python3 translation-skill/scripts/batch_croissant.py --input-file data/final_translations.csv --index-file data/index_cache.json --output-dir output/
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

## Project Structure

- `translation-skill/scripts/`: Core logic for scraping, translation, and metadata generation.
- `translation-skill/prompts/`: Markdown-based prompt templates for LLM agents.
- `training/`: Model training scripts (spaCy NER and Transformers).
- `data/`: Input and output CSV files.
- `output/`: Generated Croissant metadata and SKOS vocabularies.
- `agents.md`: Detailed documentation on agent architecture and prompts.

## Training Models

The project includes two training approaches for building custom models:

### spaCy NER Model (Recommended)

Train a lightweight Named Entity Recognition model to identify disaster terminology:

```bash
# Install spaCy
pip install spacy

# Train the model (fast, ~1-2 minutes)
python3 training/train-spacy.py --data-dir output --n-iter 30 --test

# Model saved to: training/spacy_model/
```

**Advantages:**
- Fast training (1-2 minutes)
- Small model size (~10MB)
- Works on CPU or GPU
- Production-ready

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
