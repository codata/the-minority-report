#!/usr/bin/env python3
"""hips_html_parser.py

A standalone parser that reads a HIPS Croissant metadata JSON file,
extracts the BS4 Extraction Pattern from the structured
'bs4ExtractionPattern' field (preferred) or by regex-parsing it from
the 'description' text (fallback), then interprets each pattern string
as a real BeautifulSoup4 call and applies it to the referenced HTML.

The pattern strings follow the canonical format produced by the HIPS
Croissant pipeline:

  "title":   "soup.find('title').get_text().strip()"
  "date":    "soup.find('meta', property='article:published_time')['content']
              (or name='vf:date-published-v2' / 'vf:date-published')"
  "article": "soup.find('article', class_='custom-full-content')
              (with scripts, styles, noscript, and iframe tags decomposed)"

Each string is parsed with `interpret_find_call()` to extract the tag
name and keyword attributes, then executed as a real `soup.find()` call.
The special "(or ...)" notation in the date pattern triggers a sequential
fallback across multiple selectors.  The "(with ... decomposed)" notation
in the article pattern triggers removal of those tags before text extraction.

Usage
-----
    # Parse HTML referenced by a metadata file → stdout
    python3 hips_html_parser.py --metadata hips/BI0101/output/metadata.json

    # Write to a file
    python3 hips_html_parser.py --metadata hips/BI0101/output/metadata.json \
        --output /tmp/BI0101_parsed.txt

    # Override which HTML file to parse
    python3 hips_html_parser.py --metadata hips/BI0101/output/metadata.json \
        --html hips/BI0101/data/distribution/BI0101_Airborne_Diseases.html

    # Batch all datasets under hips/
    python3 hips_html_parser.py --batch hips/ --output-dir /tmp/parsed/
"""

import argparse
import json
import os
import re
import sys

# ---------------------------------------------------------------------------
# soup.find() string interpreter
# ---------------------------------------------------------------------------

_FIND_RE = re.compile(
    r"""soup\.find\(\s*                     # soup.find(
        ['"](?P<tag>[^'"]+)['"]             # 'tag'  or  "tag"
        (?P<kwargs>[^)]*)?                  # optional keyword args
    \s*\)""",
    re.VERBOSE,
)

_KV_RE = re.compile(
    r"""(?P<key>\w+)\s*=\s*['"](?P<val>[^'"]+)['"]"""
)


def interpret_find_call(fragment: str) -> dict | None:
    """
    Parse a single ``soup.find(...)`` expression into a dict of
    ``{tag, **kwargs}`` suitable for passing to BeautifulSoup.find().

    Returns None if the fragment doesn't contain a recognisable find call.

    Examples
    --------
    >>> interpret_find_call("soup.find('title').get_text().strip()")
    {'tag': 'title'}

    >>> interpret_find_call("soup.find('meta', property='article:published_time')")
    {'tag': 'meta', 'property': 'article:published_time'}

    >>> interpret_find_call("soup.find('article', class_='custom-full-content')")
    {'tag': 'article', 'class_': 'custom-full-content'}
    """
    m = _FIND_RE.search(fragment)
    if not m:
        return None
    result = {"tag": m.group("tag")}
    kwargs_str = m.group("kwargs") or ""
    for kv in _KV_RE.finditer(kwargs_str):
        result[kv.group("key")] = kv.group("val")
    return result


def decompose_tags_from_hint(hint: str) -> list[str]:
    """
    Extract tag names from a hint like
    '(with scripts, styles, noscript, and iframe tags decomposed)'.

    Returns a list of tag name strings.
    """
    # Look for the parenthetical phrase
    m = re.search(r"\(with\s+(.+?)\s+tags?\s+decomposed\)", hint, re.IGNORECASE)
    if not m:
        return []
    raw = m.group(1)
    # Split on commas / "and"
    parts = re.split(r"[,\s]+(?:and\s+)?|(?:\s+and\s+)", raw)
    return [p.strip() for p in parts if p.strip()]


def parse_date_selectors(date_pattern: str) -> list[dict]:
    """
    Expand a date pattern string that may contain multiple selectors
    separated by "(or ...)" hints into an ordered list of find-call dicts.

    Example input:
        "soup.find('meta', property='article:published_time')['content']
         (or name='vf:date-published-v2' / 'vf:date-published')"

    Returns:
        [
            {'tag': 'meta', 'property': 'article:published_time'},
            {'tag': 'meta', 'name': 'vf:date-published-v2'},
            {'tag': 'meta', 'name': 'vf:date-published'},
        ]
    """
    selectors = []

    # Primary soup.find(...)
    primary = interpret_find_call(date_pattern)
    if primary:
        selectors.append(primary)

    # Parse the "(or name=... / ...)" fallback section
    or_match = re.search(r"\(or\s+(.+?)\)", date_pattern, re.IGNORECASE | re.DOTALL)
    if or_match:
        or_body = or_match.group(1)  # e.g. "name='vf:date-published-v2' / 'vf:date-published'"

        # Extract the attribute name (e.g. "name")
        attr_key_m = re.match(r"(\w+)\s*=", or_body)
        attr_key = attr_key_m.group(1) if attr_key_m else "name"

        # Collect all quoted values after the key
        values = re.findall(r"['\"]([^'\"]+)['\"]", or_body)
        for val in values:
            selectors.append({"tag": primary["tag"] if primary else "meta", attr_key: val})

    return selectors


# ---------------------------------------------------------------------------
# Pattern extraction from metadata
# ---------------------------------------------------------------------------

def get_extraction_pattern(metadata: dict) -> dict:
    """
    Return the BS4 extraction pattern dict from a Croissant metadata dict.

    Priority:
      1. Structured ``"bs4ExtractionPattern"`` field at the dataset root.
      2. Regex-parsed from the ``"description"`` free-text field.
      3. Built-in default (known HIPS structure).
    """
    # 1 — structured field
    structured = metadata.get("bs4ExtractionPattern")
    if structured and all(structured.get(k) for k in ("title", "date", "summary", "article", "fulltext")):
        return {"source": "bs4ExtractionPattern field", **structured}

    # 2 — parse from description text
    description = metadata.get("description", "")
    step_re = re.compile(
        r"\(\d+\)\s*(?:Title|Date|Article(?:\s+Content)?)\s*:\s*([^,;\n]+(?:,[^;\n]+)*?)(?=\s*\(\d+\)|$)",
        re.IGNORECASE,
    )
    steps = step_re.findall(description)
    if len(steps) >= 3:
        return {
            "source": "description text (parsed)",
            "title":   steps[0].strip().rstrip(","),
            "date":    steps[1].strip().rstrip(","),
            "article": steps[2].strip().rstrip("."),
        }

    # 3 — fallback default
    return {
        "source": "built-in default",
        "title":   "soup.find('title').get_text().strip()",
        "date":    "soup.find('meta', property='article:published_time')['content'] "
                   "(or name='vf:date-published-v2' / 'vf:date-published')",
        "article": "soup.find('article', class_='custom-full-content') "
                   "(with scripts, styles, noscript, and iframe tags decomposed)",
    }


# ---------------------------------------------------------------------------
# HTML parsing driven by the pattern
# ---------------------------------------------------------------------------

def parse_html(html_path: str, pattern: dict) -> dict:
    """
    Parse an HTML file using selectors derived from *pattern*.

    *pattern* is the dict returned by ``get_extraction_pattern()`` —
    its string values are ``soup.find(...)`` expression strings that
    this function interprets and executes.

    Returns a dict with keys:
      'html_path', 'title', 'date', 'summary', 'article_text', 'fulltext'
    """
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("ERROR: beautifulsoup4 is not installed.  Run: pip install beautifulsoup4",
              file=sys.stderr)
        sys.exit(1)

    with open(html_path, "r", encoding="utf-8", errors="replace") as fh:
        soup = BeautifulSoup(fh.read(), "html.parser")

    # ── 1. Title ──────────────────────────────────────────────────────────
    title = ""
    title_spec = interpret_find_call(pattern.get("title", ""))
    if title_spec:
        tag = title_spec.pop("tag")
        el = soup.find(tag, **title_spec)
        if el:
            title = el.get_text().strip()

    # ── 2. Date ───────────────────────────────────────────────────────────
    date = ""
    for selector in parse_date_selectors(pattern.get("date", "")):
        tag = selector.pop("tag")
        el = soup.find(tag, **selector)
        if el and el.get("content"):
            date = el["content"].strip()
            break

    # ── 3. Summary (Definition field) ─────────────────────────────────────
    # Pattern: soup.find('div', class_='field--name-body').find(class_='field--item')
    summary = ""
    summary_pat = pattern.get("summary", "")
    summary_spec = interpret_find_call(summary_pat)
    if summary_spec:
        tag = summary_spec.pop("tag")
        outer = soup.find(tag, **summary_spec)
        if outer:
            # Look for a chained .find(class_='field--item')
            inner_cls_match = re.search(r"\.find\(class_=['\"]([^'\"]+)['\"]\)", summary_pat)
            if inner_cls_match:
                inner_cls = inner_cls_match.group(1)
                inner = outer.find(class_=inner_cls)
                if inner:
                    summary = inner.get_text().strip()
            else:
                summary = outer.get_text().strip()

    # ── 4. Article content (main column, col-md-9) ────────────────────────
    # Pattern: soup.find('article',...).find('div', class_='col-md-9')
    article_text = ""
    article_pat = pattern.get("article", "")
    article_spec = interpret_find_call(article_pat)

    if article_spec:
        tag = article_spec.pop("tag")
        article_el = soup.find(tag, **article_spec)
    else:
        article_el = None

    # Check for a chained .find('div', class_='col-md-9') in the pattern
    col_match = re.search(r"\.find\(['\"]div['\"],\s*class_=['\"]col-md-9['\"]\)", article_pat)
    if article_el and col_match:
        scoped = article_el.find("div", class_="col-md-9")
        if scoped:
            article_el = scoped

    if not article_el:
        article_el = soup.find("article") or soup.find(class_="main-container") or soup

    decompose = decompose_tags_from_hint(article_pat) or ["script", "style", "noscript", "iframe"]
    for boilerplate in article_el(decompose):
        boilerplate.decompose()

    raw = article_el.get_text()
    lines = []
    for line in raw.splitlines():
        line = line.strip()
        if line:
            line = re.sub(r"\s+", " ", line)
            lines.append(line)
    article_text = "\n".join(lines)

    # ── 5. Full text (complete article, incl. sidebar) ────────────────────
    fulltext = ""
    fulltext_pat = pattern.get("fulltext", "")
    if fulltext_pat:
        ft_spec = interpret_find_call(fulltext_pat)
        if ft_spec:
            # Re-parse the soup so we haven't lost content from step 4 decompose
            with open(html_path, "r", encoding="utf-8", errors="replace") as fh2:
                soup2 = BeautifulSoup(fh2.read(), "html.parser")
            ft_tag = ft_spec.pop("tag")
            ft_el = soup2.find(ft_tag, **ft_spec)
            if ft_el:
                ft_decompose = decompose_tags_from_hint(fulltext_pat) or ["script", "style", "noscript", "iframe"]
                for bp in ft_el(ft_decompose):
                    bp.decompose()
                raw_ft = ft_el.get_text()
                ft_lines = []
                for line in raw_ft.splitlines():
                    line = line.strip()
                    if line:
                        line = re.sub(r"\s+", " ", line)
                        ft_lines.append(line)
                fulltext = "\n".join(ft_lines)

    return {
        "html_path":    html_path,
        "title":        title,
        "date":         date,
        "summary":      summary,
        "article_text": article_text,
        "fulltext":     fulltext,
    }


def format_output(parsed: dict) -> str:
    """Format extracted fields into clean structured text with labelled sections."""
    parts = []
    parts.append(f"Title: {parsed['title']}")
    if parsed.get("date"):
        parts.append(f"Date: {parsed['date']}")
    if parsed.get("summary"):
        parts.append("\nSummary:")
        parts.append(parsed["summary"])
    if parsed.get("article_text"):
        parts.append("\nArticle Content:")
        parts.append(parsed["article_text"])
    if parsed.get("fulltext"):
        parts.append("\nFull Text:")
        parts.append(parsed["fulltext"])
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# HTML file discovery from metadata
# ---------------------------------------------------------------------------

def find_html_files_in_metadata(metadata: dict, metadata_dir: str) -> list[str]:
    """
    Return absolute paths to HTML files referenced in a Croissant metadata dict.
    Checks both 'isBasedOn' and 'distribution'; skips embedded data URIs.
    """
    html_paths = []

    def resolve(url: str) -> str | None:
        if not url or url.startswith("data:"):
            return None
        path = url if os.path.isabs(url) else \
               os.path.normpath(os.path.join(metadata_dir, url))
        return path if os.path.isfile(path) else None

    based_on = metadata.get("isBasedOn", [])
    if isinstance(based_on, dict):
        based_on = [based_on]
    for item in based_on:
        if isinstance(item, dict):
            if item.get("encodingFormat") == "text/html" or \
               item.get("name", "").endswith(".html"):
                p = resolve(item.get("contentUrl", ""))
                if p:
                    html_paths.append(p)

    for item in metadata.get("distribution", []):
        if isinstance(item, dict):
            if item.get("encodingFormat") == "text/html" or \
               item.get("name", "").endswith(".html"):
                p = resolve(item.get("contentUrl", ""))
                if p:
                    html_paths.append(p)

    return html_paths


# ---------------------------------------------------------------------------
# Main entry points
# ---------------------------------------------------------------------------

def run_single(metadata_path: str, html_override: str | None, output_path: str | None):
    """Parse HTML referenced by (or overriding) a single metadata file."""
    metadata_dir = os.path.dirname(os.path.abspath(metadata_path))

    with open(metadata_path, "r", encoding="utf-8") as fh:
        metadata = json.load(fh)

    pattern = get_extraction_pattern(metadata)
    print(f"Pattern source : {pattern['source']}")
    print(f"  title   → {pattern.get('title',   '(missing)')[:80]}")
    print(f"  date    → {pattern.get('date',    '(missing)')[:80]}")
    print(f"  article → {pattern.get('article', '(missing)')[:80]}")
    print()

    # Show interpreted selectors so the user can verify
    title_spec   = interpret_find_call(pattern.get("title", ""))
    date_specs   = parse_date_selectors(pattern.get("date", ""))
    article_spec = interpret_find_call(pattern.get("article", ""))
    decompose    = decompose_tags_from_hint(pattern.get("article", "")) or ["script","style","noscript","iframe"]
    print("Interpreted selectors:")
    print(f"  title   → soup.find({title_spec})")
    print(f"  date    → {date_specs}  (tried in order)")
    print(f"  article → soup.find({article_spec})  decompose={decompose}")
    print()

    html_files = [html_override] if html_override else \
                 find_html_files_in_metadata(metadata, metadata_dir)

    if not html_files:
        print("No HTML files found in metadata or specified via --html.", file=sys.stderr)
        sys.exit(1)

    for html_path in html_files:
        print(f"Parsing: {html_path}")
        parsed = parse_html(html_path, dict(pattern))
        text = format_output(parsed)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print(f"  → Written to {output_path}")
        else:
            print("\n" + "=" * 60)
            print(text)
            print("=" * 60 + "\n")


def run_batch(hips_root: str, output_dir: str):
    """Batch-parse all HTML files across all HIPS dataset metadata files."""
    import glob

    pattern_glob = os.path.join(os.path.abspath(hips_root), "*", "output", "metadata.json")
    metadata_files = sorted(glob.glob(pattern_glob))
    print(f"Found {len(metadata_files)} metadata files under {hips_root}")

    os.makedirs(output_dir, exist_ok=True)

    ok = skipped = errors = 0
    for mpath in metadata_files:
        hips_code = os.path.basename(os.path.dirname(os.path.dirname(mpath)))
        metadata_dir = os.path.dirname(mpath)

        try:
            with open(mpath, "r", encoding="utf-8") as fh:
                metadata = json.load(fh)
        except Exception as e:
            print(f"  SKIP {hips_code}: could not read metadata ({e})")
            skipped += 1
            continue

        html_files = find_html_files_in_metadata(metadata, metadata_dir)
        if not html_files:
            print(f"  SKIP {hips_code}: no HTML file found")
            skipped += 1
            continue

        try:
            pattern = get_extraction_pattern(metadata)
            parsed  = parse_html(html_files[0], dict(pattern))
            text    = format_output(parsed)
            out_path = os.path.join(output_dir, hips_code + "_parsed.txt")
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print(f"  ✓ {hips_code} [{pattern['source']}] → {out_path}")
            ok += 1
        except Exception as e:
            print(f"  ERROR {hips_code}: {e}")
            errors += 1

    print(f"\nDone. OK: {ok} | Skipped: {skipped} | Errors: {errors}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Parse HIPS HTML files using the BS4 Extraction Pattern "
            "read directly from a Croissant metadata JSON file."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--metadata", "-m",
        metavar="METADATA_JSON",
        help="Path to a single Croissant metadata JSON file.",
    )
    mode.add_argument(
        "--batch", "-b",
        metavar="HIPS_ROOT",
        help="Path to the hips/ root directory for batch processing.",
    )
    parser.add_argument(
        "--html",
        metavar="HTML_FILE",
        help="(single mode only) Override the HTML file to parse.",
    )
    parser.add_argument(
        "--output", "-o",
        metavar="OUTPUT_FILE",
        help="(single mode) Write parsed text here instead of stdout.",
    )
    parser.add_argument(
        "--output-dir",
        metavar="OUTPUT_DIR",
        default="./parsed_hips",
        help="(batch mode) Directory for output .txt files (default: ./parsed_hips).",
    )
    args = parser.parse_args()

    if args.metadata:
        run_single(args.metadata, args.html, args.output)
    else:
        run_batch(args.batch, args.output_dir)


if __name__ == "__main__":
    main()
