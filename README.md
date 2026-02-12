# The Minority Report

A set of tools for multilingual concept translation, alignment, and metadata generation using Large Language Models (LLMs). This project is designed to help researchers and data stewards enrich vocabularies and datasets with high-quality, AI-generated translations and Croissant-compliant metadata.

## Features
- **Orchestrator**: Manages translation tasks across multiple LLM models and languages.
- **Consensus & Arbitration**: Ensures high-quality translations by requiring model consensus or using an arbitrator model.
- **Croissant Metadata**: Generates ML-ready metadata for your datasets.
- **Dataverse Integration**: (Optional) Tools to publish enriched datasets to Dataverse.
- **MCP Server**: Provides Model Context Protocol (MCP) compatible tools for seamless integration with AI agents.

## Installation

### Prerequisites

1.  **Python 3.10+** (Required)

2.  **Ollama**: Install [Ollama](https://ollama.ai/) to run local LLMs.
    
    **macOS / Linux:**
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

    **Windows:**
    Download from [ollama.com](https://ollama.com).

    **Models:**
    Pull the models you intend to use before running the tool:
    ```bash
    ollama pull llama3
    ollama pull mistral
    ```
    Ensure Ollama is running (`ollama serve`).

### Install Package
Clone the repository and install the package in editable mode:

```bash
pip install -e .
```
(We recommend using a virtual environment: `python3 -m venv venv && source venv/bin/activate`)

## Setup & Configuration

### Configure Endpoints
Use the `rosettastone-init` command to configure your Ollama connection.

```bash
rosettastone-init
```

Follow the prompts to enter your Ollama host URL (default: `http://localhost:11434`).
- If running locally: `http://localhost:11434`
- If using a remote server: `http://<ip>:11434`

## Usage

### Run Orchestrator
Translate a term manually:
```bash
rosettastone-orchestrator --concept "Avalanche" --context "A rapid flow of snow down a slope." --languages fr,es --models llama3
```

Scrape and translate from a URL:
```bash
rosettastone-orchestrator --url https://example.com/term --languages fr,es,de
```

### Generate Metadata
(Integrated into Orchestrator, but can be run separately if needed)
```bash
python3 the_minority_report/croissant_generator.py --help
```

## MCP Server

This package provides an MCP server that exposes translation and scraping capabilities to compatible AI agents.

To run the MCP server:
```bash
# Assuming you have fastmcp installed or using uv
uvx fastmcp run translation-skill/scripts/mcp_server.py
# Or if installed:
python3 translation-skill/scripts/mcp_server.py
```

Available Tools:
- `understand_and_translate(term, context, languages, models)`: Translates a specific term.
- `open_page_and_translate(url, languages, models)`: Scrapes a URL and translates the term found.
- `find_hazards(query)`: Analyzes text for hazard terminology.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
