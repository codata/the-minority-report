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
    python3 benchmark-skill/scripts/benchmark.py \
      --google-sheet "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/..." \
      --translations-csv "data/final_translations.csv" \
      --mismatches-output "mismatches.csv"
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
