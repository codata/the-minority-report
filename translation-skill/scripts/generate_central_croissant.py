"""generate_central_croissant.py

Creates a central Croissant metadata file that acts as a navigable catalog
of all per-dataset Croissant files under hips/*/output/metadata.json.

Each per-dataset file is represented as a cr:FileObject in the distribution
section, with a clear AI-readable description so that models can discover
and access individual datasets without scanning the whole file tree.

Usage
-----
    python3 generate_central_croissant.py \
        [--hips-root   /path/to/hips]          # default: auto-detected
        [--output-file /path/to/central.json]  # default: hips/../central_metadata.json
        [--embed]                              # embed files as base64 (LARGE!)
"""

import json
import os
import sys
import hashlib
import datetime
import argparse
import base64
import glob

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
HIPS_ROOT_DEFAULT = os.path.join(
    os.path.dirname(__file__), "..", "..", "hips"
)
OUTPUT_DEFAULT = os.path.join(
    os.path.dirname(__file__), "..", "..", "hips", "central_metadata.json"
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def compute_sha256(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return "UNREADABLE"


def read_as_data_uri(path, mime="application/ld+json"):
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode('ascii')}"


def dataset_description(hips_code, term_name, num_records, languages):
    """Generate an AI-readable description for a single dataset entry."""
    lang_str = ", ".join(sorted(languages)) if languages else "unknown"
    pw_url = (
        f"https://www.preventionweb.net/understanding-disaster-risk/"
        f"terminology/hips/{hips_code.lower()}"
    )
    return (
        f"Croissant dataset for UNDRR/ISC Hazard Information Profile "
        f"{hips_code}: \"{term_name}\". "
        f"Contains multilingual translations of the hazard term in language(s): "
        f"{lang_str}. "
        f"Each record includes the source term, its contextual definition, the "
        f"translated term, language code (ISO 639-1), confidence score, "
        f"generating LLM model, consensus status, and version. "
        f"The distribution section links/embeds the original UNDRR/ISC HIPS HTML "
        f"page from {pw_url} (which contains the authoritative SKOS definition and "
        f"metadata sections), along with an additionally generated clean plaintext version "
        f"that strips Drupal headers, footers, navigation, styles, and scripts. "
        f"Approx. {num_records} translation record(s). "
        f"License: CC BY 4.0."
    )


def extract_dataset_info(metadata_path):
    """
    Read a per-dataset metadata.json and extract key fields for the catalog.

    Returns a dict with keys: hips_code, term_name, num_records, languages,
    has_html, sha256.
    """
    info = {
        "hips_code": None,
        "term_name": None,
        "num_records": 0,
        "languages": [],
        "has_html": False,
        "sha256": compute_sha256(metadata_path),
    }

    try:
        d = json.load(open(metadata_path))
    except Exception:
        return info

    # HIPS code from schema:identifier or directory name
    info["hips_code"] = (
        d.get("https://schema.org/identifier")
        or os.path.basename(os.path.dirname(os.path.dirname(metadata_path)))
    )

    # Term name: try top-level name, strip "Multilingual Dataset" fallback
    name = d.get("name", "")
    if name and name != "Multilingual Dataset":
        info["term_name"] = name
    else:
        # Derive from HIPS code + isBasedOn HTML filename
        based_on = d.get("isBasedOn", [])
        if isinstance(based_on, dict):
            based_on_list = [based_on]
        elif isinstance(based_on, list):
            based_on_list = based_on
        else:
            based_on_list = []

        for item in based_on_list:
            if isinstance(item, dict):
                fname = item.get("name", "")
                if fname.endswith(".html"):
                    parts = os.path.splitext(fname)[0].split("_", 1)
                    if len(parts) > 1:
                        info["term_name"] = parts[1].replace("_", " ")
                    break
        
        if not info["term_name"]:
            # Fallback to distribution HTML filename
            for item in d.get("distribution", []):
                fname = item.get("name", "")
                if fname.endswith(".html"):
                    parts = os.path.splitext(fname)[0].split("_", 1)
                    if len(parts) > 1:
                        info["term_name"] = parts[1].replace("_", " ")
                    break
        if not info["term_name"]:
            info["term_name"] = info["hips_code"] or "Unknown"

    # Check for HTML in isBasedOn or distribution
    based_on = d.get("isBasedOn", [])
    if isinstance(based_on, dict):
        based_on_list = [based_on]
    elif isinstance(based_on, list):
        based_on_list = based_on
    else:
        based_on_list = []

    for item in based_on_list:
        if isinstance(item, dict):
            if item.get("encodingFormat") == "text/html" or item.get("name", "").endswith(".html"):
                info["has_html"] = True

    for item in d.get("distribution", []):
        url = item.get("contentUrl", "")
        fmt = item.get("encodingFormat", "")
        name = item.get("name", "")
        if "data:text/html" in url or fmt == "text/html" or name.endswith(".html"):
            info["has_html"] = True

    # Try to read languages from the sibling CSV
    csv_path = None
    for item in d.get("distribution", []):
        if item.get("encodingFormat") == "text/csv":
            csv_path = item.get("contentUrl", "")
            break

    if csv_path:
        if not os.path.isabs(csv_path):
            csv_path = os.path.normpath(os.path.join(os.path.dirname(metadata_path), csv_path))

    if csv_path and os.path.isfile(csv_path):
        try:
            import csv as _csv
            langs = set()
            with open(csv_path, newline="", encoding="utf-8") as cf:
                reader = _csv.DictReader(cf)
                for row in reader:
                    info["num_records"] += 1
                    if "language" in row and row["language"]:
                        langs.add(row["language"].strip())
            info["languages"] = sorted(langs)
        except Exception:
            pass

    return info


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------

def build_central_croissant(hips_root, output_file, embed=False):
    hips_root = os.path.abspath(hips_root)
    output_file = os.path.abspath(output_file)

    pattern = os.path.join(hips_root, "*", "output", "metadata.json")
    metadata_files = sorted(glob.glob(pattern))

    print(f"Found {len(metadata_files)} per-dataset Croissant files.")

    distribution = []
    total_html = 0

    for mpath in metadata_files:
        hips_code = os.path.basename(os.path.dirname(os.path.dirname(mpath)))
        print(f"  Processing {hips_code} …", end=" ", flush=True)

        info = extract_dataset_info(mpath)

        # Prefer discovered HIPS code over directory name
        code      = info["hips_code"] or hips_code
        term_name = info["term_name"] or hips_code
        desc      = dataset_description(
            code, term_name, info["num_records"], info["languages"]
        )

        obj_id = f"dataset_{code}"

        if embed:
            content_url = read_as_data_uri(mpath)
        else:
            # Relative path from the output_file location
            content_url = os.path.relpath(mpath, os.path.dirname(output_file))

        entry = {
            "@type": "cr:FileObject",
            "@id": obj_id,
            "name": f"{code}_{term_name.replace(' ', '_')}",
            "description": desc,
            "contentUrl": content_url,
            "encodingFormat": "application/ld+json",
            "sha256": info["sha256"],
        }

        # Add convenience flags for quick filtering by AI tools
        entry["cr:hasPart"] = {
            "htmlEmbedded": info["has_html"],
            "languages": info["languages"],
            "approxRecords": info["num_records"],
            "hipsCode": code,
        }

        # Find HTML and clean text files in the dataset directory
        html_file = None
        html_sha256 = None
        txt_file = None
        txt_sha256 = None
        dataset_dir = os.path.dirname(os.path.dirname(mpath))
        dist_dir = os.path.join(dataset_dir, "data", "distribution")
        if os.path.isdir(dist_dir):
            for fname in os.listdir(dist_dir):
                if fname.endswith(".html"):
                    html_file = os.path.normpath(os.path.join(dist_dir, fname))
                    html_sha256 = compute_sha256(html_file)
                elif fname.endswith("_clean.txt"):
                    txt_file = os.path.normpath(os.path.join(dist_dir, fname))
                    txt_sha256 = compute_sha256(txt_file)

        # Generate entries for isBasedOn list
        is_based_on_list = []
        if html_file:
            html_rel_path = os.path.relpath(html_file, os.path.dirname(output_file))
            
            # Formulate the description with the HTML parsing tips
            source_url = f"https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/{code.lower()}"
            html_desc = (
                f"Original UNDRR/ISC Hazard Information Profile HTML page for {code}: \"{term_name}\". "
                f"Preserves full authoritative content as published at {source_url}. "
                f"Parsing Tip: The core technical content can be extracted from the HTML structure by targeting the "
                f"<article class='custom-full-content'> (or fallback <div class='main-container'>) container and decomposing "
                f"boilerplate script, style, noscript, and iframe tags. Section titles follow repeated patterns: major sections "
                f"use <h2> and <h3> tags with class 'field-label-above' or 'field-group-title' (e.g., 'Primary reference(s)', "
                f"'Annotations', 'Drivers', 'Impacts', 'Risk Management', 'Monitoring', 'References'), and inline field labels "
                f"use <div> with class 'field--label' or 'field-label-inline' (e.g., 'Unique identifier / Notation', 'Synonyms', "
                f"'Definition')."
            )
            is_based_on_list.append({
                "@type": "CreativeWork",
                "@id": f"html_{code}",
                "name": os.path.basename(html_file),
                "description": html_desc,
                "contentUrl": html_rel_path,
                "encodingFormat": "text/html",
                "sha256": html_sha256,
            })
            
        if txt_file:
            txt_rel_path = os.path.relpath(txt_file, os.path.dirname(output_file))
            is_based_on_list.append({
                "@type": "CreativeWork",
                "@id": f"text_{code}",
                "name": os.path.basename(txt_file),
                "description": (
                    f"Clean plaintext extract of the original HIPS HTML document for {code}: \"{term_name}\", "
                    f"omitting template headers, footers, navigation, styles, and scripts. "
                    f"BS4 Extraction Pattern: "
                    f"(1) Title: soup.find('title').get_text().strip(), "
                    f"(2) Date: soup.find('meta', property='article:published_time')['content'] (or name='vf:date-published-v2' / 'vf:date-published'), "
                    f"(3) Article Content: soup.find('article', class_='custom-full-content') (scripts, styles, noscript, and iframe tags decomposed)."
                ),
                "contentUrl": txt_rel_path,
                "encodingFormat": "text/plain",
                "sha256": txt_sha256,
            })

        if is_based_on_list:
            entry["isBasedOn"] = is_based_on_list

        distribution.append(entry)

        if info["has_html"]:
            total_html += 1
        print("✓")

    # Build the central Croissant document
    central = {
        "@context": {
            "@language": "en",
            "@vocab": "https://schema.org/",
            "cr":  "http://mlcommons.org/croissant/",
            "dct": "http://purl.org/dc/terms/",
            "sc":  "https://schema.org/",
            "conformsTo": "dct:conformsTo",
            "distribution": {"@id": "cr:distribution"},
            "bs4ExtractionPattern": {
                "@id": "sc:processingRequirement",
                "@type": "@json"
            },
        },
        "@type": "sc:Dataset",
        "name": "UNDRR-ISC Hazard Information Profiles — Multilingual Translation Dataset",
        "description": (
            "Central Croissant catalog for the UNDRR/ISC Hazard Information "
            "Profiles (HIPS) multilingual translation project. "
            "This file provides navigable references to all per-dataset "
            "Croissant metadata files. Each entry in the 'distribution' section "
            "corresponds to one HIPS concept and contains: (1) the translated "
            "terminology CSV (term, context, translation, language, confidence, "
            "model, consensus, version); (2) the original UNDRR/ISC HTML page "
            "for that hazard, base64-embedded or relatively linked, alongside "
            "its clean plaintext extract omitting boilerplate headers/footers; "
            "and (3) full provenance metadata (SKOS, JSON-LD, CC BY 4.0). "
            "BS4 Extraction Pattern (generic for all HIPS HTML pages): "
            "(1) Title: soup.find('title').get_text().strip(), "
            "(2) Date: soup.find('meta', property='article:published_time')['content'] (or name='vf:date-published-v2' / 'vf:date-published'), "
            "(3) Article Content: soup.find('article', class_='custom-full-content') (with scripts, styles, noscript, and iframe tags decomposed). "
            "Generated by the Minority Report translation pipeline using multiple "
            "LLM agents (Gemini, GPT, DeepSeek, Gemma) with consensus arbitration. "
            "Source vocabulary: https://www.preventionweb.net/drr-glossary/hips"
        ),
        "conformsTo": "http://mlcommons.org/croissant/1.0",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "version": "1.0.0",
        "datePublished": datetime.datetime.utcnow().isoformat(),
        "publisher": {
            "@type": "sc:Organization",
            "name": "CODATA / The Minority Report Project",
        },
        "keywords": [
            "UNDRR", "HIPS", "hazard information profiles",
            "multilingual", "controlled vocabulary", "disaster risk",
            "translations", "NLP", "AI dataset", "Croissant"
        ],
        "url": "https://github.com/codata/the-minority-report",
        "bs4ExtractionPattern": {
            "title":    "soup.find('title').get_text().strip()",
            "date":     "soup.find('meta', property='article:published_time')['content'] (or name='vf:date-published-v2' / 'vf:date-published')",
            "summary":  "soup.find('div', class_='field--name-body').find(class_='field--item').get_text().strip()",
            "article":  "soup.find('article', class_='custom-full-content').find('div', class_='col-md-9') (with scripts, styles, noscript, and iframe tags decomposed)",
            "fulltext": "soup.find('article', class_='custom-full-content') (with scripts, styles, noscript, and iframe tags decomposed)"
        },
        "distribution": distribution,
        # Quick-access summary for AI tools
        "cr:recordSet": {
            "@type": "cr:RecordSet",
            "@id": "catalog_index",
            "name": "Dataset Index",
            "description": (
                "Index of all HIPS datasets in this collection. "
                f"Total datasets: {len(distribution)}. "
                f"Datasets with embedded HTML source: {total_html}."
            ),
        }
    }

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(central, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Central Croissant file written to: {output_file}")
    print(f"   Datasets referenced : {len(distribution)}")
    print(f"   With embedded HTML  : {total_html}")
    size_kb = os.path.getsize(output_file) / 1024
    print(f"   File size           : {size_kb:.1f} KB")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate a central Croissant catalog for all HIPS datasets."
    )
    parser.add_argument(
        "--hips-root", default=HIPS_ROOT_DEFAULT,
        help="Path to the hips/ directory (default: auto-detected)"
    )
    parser.add_argument(
        "--output-file", default=OUTPUT_DEFAULT,
        help="Path for the output central_metadata.json"
    )
    parser.add_argument(
        "--embed", action="store_true",
        help="Embed individual Croissant files as base64 data URIs (produces a very large file)"
    )
    args = parser.parse_args()

    build_central_croissant(
        hips_root=args.hips_root,
        output_file=args.output_file,
        embed=args.embed,
    )


if __name__ == "__main__":
    main()
