# Translation Benchmarking

This project includes a comprehensive benchmarking skill to evaluate the quality of system-generated translations against a manual ground truth (Google Sheet).

## Overview
The benchmark compares translations row-by-row for matched English terms. It supports multiple languages (French, Spanish, Chinese) and provides detailed metrics to assess both exact correctness and semantic equivalence.

## Methodology & Metrics

We employ three distinct metrics to evaluate translation quality:

### 1. Exact Match
- **Definition**: The percentage of terms where the system translation is identical to the human translation.
- **Normalization**: Both strings are normalized before comparison:
    - Converted to lowercase.
    - Punctuation removed.
    - Diacritics/accents stripped (e.g., "bébé" == "bebe").
- **Interpretation**: A high exact match rate indicates high consistency with the specific vocabulary used in the ground truth.

### 2. Lexical Similarity
- **Definition**: Uses `difflib.SequenceMatcher` to calculate a normalized Levenshtein distance similarity (0-100%).
- **Interpretation**: Captures how close the spelling and structure are. Useful for detecting minor typos or morphological variations that Exact Match misses.

### 3. Semantic Similarity
- **Definition**: Uses state-of-the-art Sentence Transformers (default: `paraphrase-multilingual-MiniLM-L12-v2`) to compute the cosine similarity between the vector embeddings of the system and human translations.
- **Interpretation**: Captures **meaning**. A high semantic score with a low lexical score indicates a valid paraphrase (e.g., "Global Warming" vs "Climate Change"). This is often the most important metric for machine translation utility.

### 4. BLEU Score (Optional)
- **Definition**: Standard metric for machine translation that counts n-gram overlaps. Uses `sacrebleu`.
- **Interpretation**:
    - **> 40**: High quality, often indistinguishable from human.
    - **30-40**: Good quality, understandable.
    - **20-30**: Fair quality, understandable but with grammatical errors.
    - **< 20**: Limited utility, major errors.
    - *Note*: BLEU penalizes paraphrases and is sensitive to tokenization (especially for Chinese).

### 5. COMET Score (Optional)
- **Definition**: Neural metric (`wmt22-comet-da`) that predicts translation quality based on source, translation, and reference.
- **Interpretation**:
    - **> 0.85**: Excellent (often better than human-human agreement).
    - **0.75-0.85**: Good (high quality, minor errors).
    - **< 0.7**: Significant errors or completely different meaning.
    - *Note*: COMET is much more reliable than BLEU for semantic accuracy, especially for distant language pairs like Chinese-English.

## Running the Benchmark

### Option 1: Docker (Recommended)
The benchmark is integrated into the common Docker environment.

```bash
docker-compose run benchmark
```
This will:
1.  Build the image with all dependencies.
2.  Run the benchmark against the default Google Sheet and `data/final_translations.csv`.
3.  Output the report to `benchmark_report.md`.

### Option 2: Local Execution
Requires Python 3.10+ and dependencies.

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run Script**:
    ```bash
    ```bash
    rosettastone-benchmark \
      --google-sheet "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/..." \
      --translations-csv "data/final_translations.csv" \
      --mismatches-output "mismatches.csv" \
      --use-bleu \
      --use-comet
    ```

## Configuration

You can customize the benchmark using arguments and environment variables:

### Filtering
- **`--max-words N`**: Filter the ground truth to only include English terms with `N` words or fewer. Useful for focusing on terminology vs long definitions.
    - Default: `3`
    - Example: `docker-compose run benchmark --max-words 5`

### Semantic Model
- **`SENTENCE_TRANSFORMER_MODEL`**: Set this environment variable to use a different Hugging Face model.
    - Default: `paraphrase-multilingual-MiniLM-L12-v2`
    - Example (in `.env` or docker-compose): `contextual-multilingual-e5-base`

### Output
- **`benchmark_report.md`**: A summary Markdown report with stats per language.
- **`mismatches.csv`**: (Optional) A CSV file listing every mismatch with its scores, useful for deep-dive analysis.

## Files
- **Script**: `benchmark-skill/scripts/benchmark.py`
- **Docker**: Uses the root `Dockerfile` and `docker-compose.yml`.
