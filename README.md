# Multilingual Controlled Vocabulary Pipeline

An agentic pipeline for generating high-quality multilingual technical translations and controlled vocabularies. The project uses a multi-model approach (Voter/Arbitrator architecture) to translate terms while preserving context and generating standard [Croissant](http://mlcommons.org/croissant/) metadata.

## Features

- **Multi-Model Orchestration**: Leverages `gpt-oss:latest`, `gemma3:27b`, and `deepseek-r1:14b` via Ollama.
- **Context-Aware Translation**: Uses "Scope Notes" to ensure technical accuracy.
- **Web Scraping**: Built-in support for extracting terms and definitions from sites like PreventionWeb.
- **Formal Provenance**: Every translation is linked to its source model in both CSV and Croissant metadata.
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

### 🐍 Using Python Directly

Ensure your `OLLAMA_HOST` is set:
```bash
export OLLAMA_HOST=http://10.147.18.253:11434
python3 translation-skill/scripts/orchestrator.py --url "YOUR_URL" --output_dir data
```

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

## License
Distributed under the [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) license.
