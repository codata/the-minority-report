# The Minority Report

A set of tools for multilingual concept translation, alignment, and metadata generation using Large Language Models (LLMs). This project is designed to help researchers and data stewards enrich vocabularies and datasets with high-quality, AI-generated translations and Croissant-compliant metadata.

## Features
- **Orchestrator**: Manages translation tasks across multiple LLM models and languages.
- **Consensus & Arbitration**: Ensures high-quality translations by requiring model consensus or using an arbitrator model.
- **Croissant Metadata**: Generates ML-ready metadata for your datasets.
- **Dataverse Integration**: (Optional) Tools to publish enriched datasets to Dataverse.

## 1. Prerequisites & Ollama Setup

Before installing the python package, you must have **[Ollama](https://ollama.ai/)** installed and running. This tool allows you to run Large Language Models locally.

### Install Ollama

**macOS / Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download the installer from [ollama.com](https://ollama.com).

### Pull Required Models
You must pull the models you intend to use. The default model is `gpt-oss` (renamed or custom) or standard models like `llama3`, `mistral`, or `gemma`.

Example:
```bash
ollama pull llama3
ollama pull mistral
```
Ensure Ollama is running (`ollama serve`) before proceeding.

## 2. Installation

### Install Package
Clone the repository and install the package in editable mode:

```bash
pip install -e .
```
(We recommend using a virtual environment: `python3 -m venv venv && source venv/bin/activate`)

## 3. Configuration

### Configure Endpoints
Use the `tmr-init` command to configure your Ollama connection.

```bash
tmr-init
```

Follow the prompts to enter your Ollama host URL (default: `http://localhost:11434`).
- If running locally: `http://localhost:11434`
- If using a remote server: `http://<ip>:11434`

## Usage

### Run Orchestrator
Translate a term manually:
```bash
tmr-orchestrator --concept "Avalanche" --context "A rapid flow of snow down a slope." --languages fr,es --models llama3
```

Scrape and translate from a URL:
```bash
tmr-orchestrator --url https://example.com/term --languages fr,es,de
```

### Generate Metadata
(Integrated into Orchestrator, but can be run separately if needed)
```bash
python3 the_minority_report/croissant_generator.py --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
