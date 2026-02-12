---
name: Google Sheets Reader Skill
description: A skill to read terminology from Google Sheets.
---

# Google Sheets Reader Skill

This skill allows reading terminology lists from Google Sheets.

## Features
- Converts Google Sheet URLs to CSV export format.
- Reads `term_en` and `definition_en` columns.
- Returns a list of dictionaries compatible with the Orchestrator.

## Usage

```bash
python3 scripts/sheet_reader.py <GOOGLE_SHEET_URL>
```

## Requirements
- pandas
