# Quickstart Guide

This guide covers the end-to-end pipeline for the **The Minority Report** project: scraping terminology, translating it, generating metadata, and training models.

## Prerequisites

- **Python 3.10+**
- **Docker** (for Ollama/LLM services)
- **Ollama** running locally or remotely (default: `http://10.147.18.253:11434`)

### Install Dependencies
```bash
pip3 install -r requirements.txt
pip3 install spacy mlcroissant
# Install spaCy multilingual base
python3 -m spacy download xx_ent_wiki_sm
```

---

## 1. Build Index & Scrape Data

Scrape the "Hazard Information Profiles" (HIPS) index to create a local cache of terms and codes.

```bash
# Verify the indexer is working
python3 translation-skill/scripts/orchestrator.py --index-url https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/ --output-dir data
```
*Output: `data/index_cache.json`*

## 2. Translate Terms (Agentic Workflow)

```bash
# Basic translation
python3 translation-skill/scripts/orchestrator.py \
  --index-file data/index_cache.json \
  --languages fr,es,tr,ua,ru,ch,it,nl \
  --models gpt-oss:latest \
  --output-dir data

# Advanced: Enrich with OntoPortal Definitions (e.g. EcoPortal)
# Export your API key first:
export ONTOPORTAL_API_KEY="528c4e4a-5c3e-4798-a2e2-11d96761b8ce"

python3 translation-skill/scripts/orchestrator.py \
  --index-file data/index_cache.json \
  --ontoportal-url "http://ecoportal.lifewatch.eu:8080" \
  --models gpt-oss:latest
```

## 3. Generate Croissant Metadata

Convert the raw CSV translations into rich, machine-readable Croissant (JSON-LD) files.

```bash
python3 translation-skill/scripts/batch_croissant.py \
  --input-file data/final_translations.csv \
  --index-file data/index_cache.json \
  --output-dir output/
```
*Output: `output/croissant_*.json` (one file per term)*

## 4. Scalable Data Augmentation

Use the LLM to generate diverse, natural language training examples for every term in every language. This replaces hardcoded templates.

```bash
# Augment all files in output/ directory
python3 training/augment_data.py --data-dir output
```
*Modifies `output/croissant_*.json` in-place, adding `sc:example` fields.*

## 5. Train Models

### A. Train spaCy NER Model
Train a lightweight, fast Named Entity Recognition model to detect terms and labels (e.g., `HIPS_BI0310`, `HIPS_BI0310_TR_FR`).

**Single-job training:**
```bash
python3 training/train-spacy.py \
  --data-dir output \
  --index-file data/index_cache.json \
  --output-dir training/spacy_model \
  --n-iter 50 \
  --test
```

**Parallel training (recommended for multi-core systems):**
```bash
# Train 16 models in parallel using 16 CPU cores
python3 training/train-spacy.py \
  --data-dir output \
  --n-jobs 16 \
  --n-iter 30 \
  --output-dir training/spacy_model

# Monitor progress in real-time (in another terminal)
tail -f training/spacy_model/run_*.log
```

**Output:**
- Single-job: `training/spacy_model/` directory
- Parallel: `training/spacy_model/run_0/`, `run_1/`, ..., `run_15/` directories
- Log files: `training/spacy_model/run_0.log`, `run_1.log`, etc.

**Choosing the best model:**
```bash
# Check final loss values
tail -5 training/spacy_model/run_*.log | grep "Loss:"

# Test a specific model
python3 training/test_spacy_model.py training/spacy_model/run_0
```

### B. Fine-Tune LLM (Optional)
Fine-tune a small LLM (e.g., Gemma 2B) on the dataset for translation tasks.

```bash
python3 training/train.py \
  --data-dir output \
  --model-name google/gemma-2-2b-it \
  --output-dir training/fine_tuned_model
```

---

## Verification

To verify the pipeline works, check a generated Croissant file for `sc:example`:
```bash
grep "sc:example" output/croissant_*.json | head -n 5
```

To test the trained spaCy model:
```bash
python3 training/test_spacy_model.py training/spacy_model
```

## 6. Running Tests

To verify the integrity of the entire pipeline, including the MCP server logic:
```bash
python3 tests/test_find_hazards.py
python3 tests/test_load_index.py
python3 tests/test_json.py
```
