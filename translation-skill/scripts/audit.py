import json
import os
import sys

# --- CONFIGURATION ---
CATALOG_PATH = 'hips/semantic_croissant.json'
INDEX_CACHE_PATH = 'data/index_cache.json'
LANGUAGES = ['ar', 'ch', 'de', 'dk', 'es', 'et', 'fi', 'fr', 'hr', 'it', 'lt', 'lv', 'nl', 'no', 'pt', 'ru', 'sk', 'sl', 'sr', 'tr', 'ua']
PLACEHOLDER_PATTERN = 'CRITICAL AI AGENT INSTRUCTION'
DEFAULT_MIN_RATIO = 0.40

# Add local scripts to path so we can import the HTML parser
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)
from hips_html_parser import parse_html, get_extraction_pattern

def get_effective_ratio(lang, default_ratio=DEFAULT_MIN_RATIO):
    lang_lower = lang.lower()
    if lang_lower in ['ch', 'zh', 'zh-cn', 'zh-tw', 'jp', 'ja', 'ko']:
        return 0.10
    elif lang_lower in ['lv', 'lt', 'et', 'fi']:
        return 0.30
    else:
        return default_ratio

def identify_missing_translations():
    project_root = os.path.dirname(os.path.dirname(script_dir))
    catalog_path = os.path.join(project_root, CATALOG_PATH)
    index_cache_path = os.path.join(project_root, INDEX_CACHE_PATH)
    
    try:
        with open(index_cache_path, 'r', encoding='utf-8') as f:
            index_cache = json.load(f)
    except Exception as e:
        print(f"Error reading index cache: {e}")
        return

    # Map cache URLs to HIPS codes
    cache_by_code = {}
    for url, data in index_cache.items():
        code = url.split('/')[-1].upper()
        cache_by_code[code] = data

    try:
        with open(catalog_path, 'r', encoding='utf-8') as f:
            catalog = json.load(f)
    except Exception as e:
        print(f'Error reading catalog: {str(e)}')
        return

    datasets = [ds.get('@id', '').replace('dataset_', '') for ds in catalog.get('dataset', []) if ds.get('@id', '').startswith('dataset_')]
    if not datasets:
        datasets = [d for d in os.listdir(os.path.join(project_root, 'hips')) if os.path.isdir(os.path.join(project_root, 'hips', d)) and len(d) == 6]

    lang_stats = {lang: {'valid': 0, 'missing': 0, 'incomplete': 0, 'missing_list': [], 'incomplete_list': []} for lang in LANGUAGES}
    
    source_lengths = {}
    for code in datasets:
        if code in cache_by_code:
            source_file = os.path.join(project_root, cache_by_code[code]['source_file'])
            if os.path.exists(source_file):
                metadata = {'article': 'some_pattern'}
                pattern = get_extraction_pattern(metadata)
                parsed = parse_html(source_file, pattern)
                article_text = parsed.get('article', parsed.get('article_text', ''))
                source_lengths[code] = len(article_text.strip())
            else:
                source_lengths[code] = 0
        else:
            source_lengths[code] = 0

    print(f'Scanning all {len(datasets)} datasets for missing/incomplete translations across {len(LANGUAGES)} languages...\n')

    for code in datasets:
        input_len = source_lengths.get(code, 0)
        
        for lang in LANGUAGES:
            file_path = os.path.join(project_root, f'hips/{code}/translations/{lang}/{code}_article.md')
            
            if not os.path.exists(file_path):
                lang_stats[lang]['missing'] += 1
                lang_stats[lang]['missing_list'].append(code)
            else:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        
                    if PLACEHOLDER_PATTERN in content:
                        lang_stats[lang]['missing'] += 1
                        lang_stats[lang]['missing_list'].append(code)
                    elif len(content) <= 5: # Some files have just "{}"
                        lang_stats[lang]['incomplete'] += 1
                        lang_stats[lang]['incomplete_list'].append(code)
                    else:
                        effective_ratio = get_effective_ratio(lang)
                        required_len = effective_ratio * input_len
                        
                        if input_len > 0 and len(content) < required_len:
                            lang_stats[lang]['incomplete'] += 1
                            lang_stats[lang]['incomplete_list'].append(code)
                        else:
                            lang_stats[lang]['valid'] += 1
                except Exception:
                    lang_stats[lang]['missing'] += 1
                    lang_stats[lang]['missing_list'].append(code)

    print("### Translation Completeness Report (with Size Validation)\n")
    print("| Language Code | Valid | Incomplete (Truncated/Empty) | Missing | Completeness % |")
    print("|--------------|-------|------------------------------|---------|----------------|")
    
    total_valid = 0
    total_incomplete = 0
    total_missing = 0
    
    for lang in LANGUAGES:
        valid = lang_stats[lang]['valid']
        incomplete = lang_stats[lang]['incomplete']
        missing = lang_stats[lang]['missing']
        
        total_valid += valid
        total_incomplete += incomplete
        total_missing += missing
        
        total = valid + incomplete + missing
        pct = (valid / total * 100) if total > 0 else 0
            
        print(f"| `{lang}` | {valid} | {incomplete} | {missing} | {pct:.1f}% |")
        
    total_scanned = total_valid + total_incomplete + total_missing
    total_pct = (total_valid / total_scanned * 100) if total_scanned > 0 else 0
    
    print("\n### Summary")
    print(f"- **Total Combinations Scanned:** {total_scanned}")
    print(f"- **Overall Valid Completeness:** {total_pct:.1f}%")
    print(f"- **Total Incomplete (Truncated/Empty) Files:** {total_incomplete}")
    print(f"- **Total Missing Files:** {total_missing}")
    
if __name__ == '__main__':
    identify_missing_translations()
