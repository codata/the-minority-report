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

Run the agents to translate all terms in the index into multiple languages (e.g., French, Spanish, Russian, Chinese).

```bash
python3 translation-skill/scripts/orchestrator.py \
  --index-file data/index_cache.json \
  --languages fr,es,ru,ch,it,nl \
  --models gpt-oss:latest \
  --output-dir data
```
*Output: `data/final_translations.csv`*

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

```bash
python3 training/train-spacy.py \
  --data-dir output \
  --index-file data/index_cache.json \
  --output-dir training/spacy_model \
  --n-iter 50 \
  --test
```
*Output: `training/spacy_model` directory*

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
