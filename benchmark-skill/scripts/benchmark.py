import pandas as pd
import argparse
import sys
import os
import difflib
from functools import lru_cache

# Add project root to path to reuse google_sheets_reader if needed, 
# but for now we'll just use pandas direct read for simplicity/isolation
# or copy the URL conversion logic.

def get_google_sheet_csv_url(url):
    import re
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if not match:
        raise ValueError("Invalid Google Sheet URL")
    sheet_id = match.group(1)
    gid = "0"
    match_gid = re.search(r'[#&?]gid=([0-9]+)', url)
    if match_gid:
        gid = match_gid.group(1)
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    return text.strip().lower()

def calculate_similarity(a, b):
    return difflib.SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()

def main():
    parser = argparse.ArgumentParser(description="Benchmark translations against Google Sheet ground truth")
    parser.add_argument("--google-sheet", required=True, help="Google Sheet URL with ground truth (term_en, term_fr, etc.)")
    parser.add_argument("--translations-csv", required=True, help="Path to final_translations.csv")
    parser.add_argument("--output-report", default="benchmark_report.md", help="Path to output Markdown report")
    args = parser.parse_args()

    print(f"Reading Ground Truth from: {args.google_sheet}")
    sheet_url = get_google_sheet_csv_url(args.google_sheet)
    try:
        df_truth = pd.read_csv(sheet_url)
    except Exception as e:
        print(f"Error reading Google Sheet: {e}")
        sys.exit(1)

    print(f"Reading System Translations from: {args.translations_csv}")
    try:
        df_sys = pd.read_csv(args.translations_csv)
    except Exception as e:
        print(f"Error reading translations CSV: {e}")
        sys.exit(1)

    # Normalize system dataframe for lookup
    # Map: (term_normalized, lang_code) -> translation
    system_translations = {}
    for _, row in df_sys.iterrows():
        term = normalize_text(row.get('term', ''))
        lang = row.get('language', '')
        trans = row.get('translation', '')
        if term and lang:
            # We store the *best* translation (highest confidence?) 
            # or just the last one if duplicates.
            # Assuming 'consensus' rows are better?
            # For now, just overwrite, assuming file is appended and latest is best.
            system_translations[(term, lang)] = trans

    # Define language mapping: Sheet Column suffix -> System Language Code
    # Sheet: term_fr -> fr
    # Sheet: term_es -> es
    # Sheet: term_zh -> ch (based on user usage)
    lang_map = {
        'fr': 'fr',
        'es': 'es',
        'zh': 'ch' # Map zh column to ch code in system
    }

    report_lines = []
    report_lines.append("# Translation Quality Benchmark Report")
    report_lines.append(f"\n**Source Sheet**: {args.google_sheet}")
    report_lines.append(f"**System File**: {args.translations_csv}")

    overall_stats = []

    for lang_suffix, sys_lang_code in lang_map.items():
        col_name = f"term_{lang_suffix}"
        if col_name not in df_truth.columns:
            print(f"Skipping {col_name} (not found in sheet)")
            continue

        print(f"Evaluating Language: {sys_lang_code} (Column: {col_name})")
        
        total = 0
        matches = 0
        total_sim = 0
        missing = 0
        mismatches = []

        for _, row in df_truth.iterrows():
            term_en = normalize_text(row.get('term_en', ''))
            truth_trans = row.get(col_name, '')
            
            if not term_en or pd.isna(truth_trans):
                continue

            truth_trans = str(truth_trans).strip()
            if not truth_trans: 
                continue

            total += 1
            
            # Lookup in system
            sys_trans = system_translations.get((term_en, sys_lang_code))
            
            if not sys_trans:
                missing += 1
                continue

            sim = calculate_similarity(sys_trans, truth_trans)
            total_sim += sim
            
            if normalize_text(sys_trans) == normalize_text(truth_trans):
                matches += 1
            else:
                if sim < 0.8: # Only log significant mismatches
                     mismatches.append({
                         "term": term_en,
                         "system": sys_trans,
                         "truth": truth_trans,
                         "score": f"{sim:.2f}"
                     })

        accuracy = (matches / total * 100) if total > 0 else 0
        avg_sim = (total_sim / (total - missing) * 100) if (total - missing) > 0 else 0
        
        stats = {
            "Language": sys_lang_code,
            "Total Terms": total,
            "Missing": missing,
            "Exact Matches": matches,
            "Accuracy (%)": f"{accuracy:.1f}%",
            "Avg Similarity (%)": f"{avg_sim:.1f}%"
        }
        overall_stats.append(stats)
        
        report_lines.append(f"\n## Language: {sys_lang_code.upper()}")
        report_lines.append(f"- **Total Manual Terms**: {total}")
        report_lines.append(f"- **Missing in System**: {missing}")
        report_lines.append(f"- **Exact Matches**: {matches} ({accuracy:.1f}%)")
        report_lines.append(f"- **Average Similarity**: {avg_sim:.1f}%")
        
        if mismatches:
            report_lines.append("\n### Top Mismatches (Similarity < 0.8)")
            report_lines.append("| Term | System | Truth | Score |")
            report_lines.append("|---|---|---|---|")
            # Sort by lowest score first
            mismatches.sort(key=lambda x: x['score'])
            for m in mismatches[:10]: # Top 10 worst
                report_lines.append(f"| {m['term']} | {m['system']} | {m['truth']} | {m['score']} |")

    # Summary Table
    report_lines.insert(4, "\n## Summary")
    summary_df = pd.DataFrame(overall_stats)
    if not summary_df.empty:
        report_lines.insert(5, summary_df.to_markdown(index=False))

    with open(args.output_report, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nReport generated: {args.output_report}")
    print(summary_df.to_string(index=False))

if __name__ == "__main__":
    main()
