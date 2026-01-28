# Dataverse Ingestion Pipeline

This directory contains scripts to convert and ingest Croissant metadata into a Dataverse repository.

## Components

- **`converter.py`**: A utility script/module that converts Croissant JSON metadata into Dataverse-compliant JSON-LD. It handles schema mapping, including the transformation of multilingual translations into Dataverse Keywords with proper language vocabulary URIs.
- **`ingest.py`**: A batch processing script that finds all `croissant_*.json` files in a specified directory, converts them using `converter.py`, and uploads them to a Dataverse instance via the API.

## Usage

### 1. Single File Conversion (Debugging)

You can run `converter.py` directly to inspect the JSON-LD output for a specific file.

```bash
python3 converter.py <path_to_croissant_file>
```

**Example:**
```bash
python3 converter.py ../output/croissant_rabies.json
```

**Output Snippet:**
```json
{
  "https://dataverse.org/schema/citation/keyword": [
    {
      "https://dataverse.org/schema/citation/keywordValue": "la rage",
      "https://dataverse.org/schema/citation/keywordVocabulary": "fr",
      "https://dataverse.org/schema/citation/keywordVocabularyURI": "https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes"
    }
  ]
}
```

### 2. Batch Ingestion

To ingest all generated metadata files into your Dataverse installation:

**Prerequisites:**
Set up your environment variables (optional, or pass as arguments):
```bash
export DATAVERSE_URL="https://demo.dataverse.org"
export DATAVERSE_ID="my-dataverse-alias"
export DATAVERSE_API_TOKEN="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

**Run command:**
```bash
python3 ingest.py --input-dir ../output
```

**Arguments:**
- `--input-dir`: Directory containing `croissant_*.json` files (default: `output`)
- `--dataverse-url`: Base URL of the Dataverse instance.
- `--dataverse-id`: Alias or ID of the parent Dataverse collection.
- `--api-token`: Your Dataverse API Token.
