# The Minority Report (formerly Rosetta AI)

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

2. **Run from a URL**:
   ```bash
   docker-compose run orchestrator --url https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/mh0103 --languages fr,es,de --models gpt-oss:latest
   ```

3. **Run from a CSV file**:
   ```bash
   docker-compose run orchestrator --input-file data/source_vocab.csv --languages fr,es
   ```

4. **Scrape an Index Page**:
   ```bash
   docker-compose run orchestrator --index-url https://www.preventionweb.net/drr-glossary/hips
   ```

5. **Generate Batch Croissant Metadata**:
   ```bash
   docker-compose run python3 translation-skill/scripts/batch_croissant.py --input-file data/final_translations.csv --output-dir output/
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
       "rosetta": {
         "command": "python3",
         "args": ["/Users/vyacheslavtykhonov/projects/rosetta-ai/translation-skill/scripts/mcp_server.py"],
         "env": {
           "OLLAMA_HOST": "http://10.147.18.253:11434"
         }
       }
     }
   }
   ```

### How to Use Rosetta AI MCP

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
- `data/`: Input and output CSV files.
- `output/`: Generated `metadata.json` (Croissant format).
- `agents.md`: Detailed documentation on agent architecture and prompts.

## Credits

- **Vyacheslav Tykhonov**: Project Lead & Architect.
- **GitHub**: [https://github.com/4tikhonov/the-minority-report](https://github.com/4tikhonov/the-minority-report)

## License
Distributed under the [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) license.
