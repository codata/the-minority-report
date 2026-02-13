import pandas as pd
import argparse
import sys
import os
import difflib
import string
import unicodedata
from functools import lru_cache

# Try to import sentence_transformers
try:
    from sentence_transformers import SentenceTransformer, util
    HAS_SEMANTIC = True
except ImportError:
    HAS_SEMANTIC = False

# Try to import sacrebleu
try:
    from sacrebleu.metrics import BLEU
    HAS_BLEU = True
except ImportError:
    HAS_BLEU = False

# Try to import comet
try:
    from comet import download_model, load_from_checkpoint
    HAS_COMET = True
except ImportError:
    HAS_COMET = False

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
    # Normalize unicode characters to decompose distinct characters
    text = unicodedata.normalize('NFD', text)
    # Filter out non-spacing mark characters (diacritics)
    text = "".join([c for c in text if unicodedata.category(c) != 'Mn'])
    # Remove punctuation and lowercase
    try:
        text = text.translate(str.maketrans('', '', string.punctuation))
    except Exception:
        pass # Handle edge cases
    return text.strip().lower()

def calculate_lexical_similarity(a, b):
    # Normalized lexical similarity
    return difflib.SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()

class SemanticMatcher:
    def __init__(self, model_name=None):
        if not HAS_SEMANTIC:
            print("Warning: sentence-transformers not installed. Semantic similarity will be 0.")
            self.model = None
            return
        
        if model_name is None:
            # Default model or from env
            model_name = os.getenv("SENTENCE_TRANSFORMER_MODEL", "paraphrase-multilingual-MiniLM-L12-v2")

        print(f"Loading semantic model: {model_name}...")
        try:
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def calculate_similarity(self, source, target):
        if not self.model or not source or not target:
            return 0.0
        
        # We process single pairs here, but batching would be faster for large datasets.
        # For ~2000 terms it's acceptable to do one by one or small batches, 
        # but to keep logic simple we'll just encode.
        # Ideally we should cache embeddings.
        embeddings = self.model.encode([source, target], convert_to_tensor=True)
        return util.cos_sim(embeddings[0], embeddings[1]).item()

def main():
    parser = argparse.ArgumentParser(description="Benchmark translations against Google Sheet ground truth")
    parser.add_argument("--google-sheet", required=True, help="Google Sheet URL with ground truth")
    parser.add_argument("--translations-csv", required=True, help="Path to final_translations.csv")
    parser.add_argument("--output-report", default="benchmark_report.md", help="Path to output Markdown report")
    parser.add_argument("--mismatches-output", help="Path to output CSV of all mismatches")
    parser.add_argument("--use-semantic", action='store_true', default=True, help="Enable semantic similarity (default: True)")
    parser.add_argument("--use-bleu", action='store_true', default=False, help="Enable BLEU score (default: False)")
    parser.add_argument("--use-comet", action='store_true', default=False, help="Enable COMET score (default: False)")
    parser.add_argument("--max-words", type=int, default=3, help="Filter terms with more than N words (default: 3)")
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

    # Initialize Semantic Matcher
    semantic_matcher = None
    if args.use_semantic and HAS_SEMANTIC:
        semantic_matcher = SemanticMatcher()

    # Initialize BLEU
    bleu_metric = None
    if args.use_bleu:
        if HAS_BLEU:
            print("Initializing BLEU metric...")
            bleu_metric = BLEU()
        else:
            print("Warning: sacrebleu not installed. Skipping BLEU.")

    # Initialize COMET
    comet_model = None
    if args.use_comet:
        if HAS_COMET:
            print("Initializing COMET model (this may download a large model)...")
            try:
                # Use a standard model
                model_path = download_model("Unbabel/wmt22-comet-da")
                comet_model = load_from_checkpoint(model_path)
            except Exception as e:
                print(f"Error loading COMET: {e}")
        else:
             print("Warning: unbabel-comet not installed. Skipping COMET.")

    # Pre-process system translations
    system_translations = {}
    for _, row in df_sys.iterrows():
        term = normalize_text(row.get('term', ''))
        lang = row.get('language', '')
        trans = row.get('translation', '')
        if term and lang:
            system_translations[(term, lang)] = trans

    lang_map = {
        'fr': 'fr',
        'es': 'es',
        'zh': 'ch' 
    }

    report_lines = []
    report_lines.append("# Translation Quality Benchmark Report")
    report_lines.append(f"\n**Source Sheet**: {args.google_sheet}")
    report_lines.append(f"**System File**: {args.translations_csv}")
    report_lines.append(f"**Max Words per Term**: {args.max_words}")
    report_lines.append(f"**Semantic/Sophisticated Matching**: {'Enabled' if semantic_matcher and semantic_matcher.model else 'Disabled'}")
    if semantic_matcher and semantic_matcher.model:
         report_lines.append(f"**Model**: {os.getenv('SENTENCE_TRANSFORMER_MODEL', 'paraphrase-multilingual-MiniLM-L12-v2')}")
         report_lines.append(f"**Semantic Threshold**: {os.getenv('SEMANTIC_SIMILARITY_THRESHOLD', '0.9')}")

    overall_stats = []
    all_mismatches = []

    for lang_suffix, sys_lang_code in lang_map.items():
        col_name = f"term_{lang_suffix}"
        if col_name not in df_truth.columns:
            print(f"Skipping {col_name}")
            continue

        print(f"Evaluating Language: {sys_lang_code} (Column: {col_name})")
        
        total = 0
        matches = 0
        total_lex_sim = 0
        total_sem_sim = 0
        missing = 0
        semantic_passes = 0
        total_passes = 0
        current_lang_mismatches = []

        try:
             sem_threshold = float(os.getenv("SEMANTIC_SIMILARITY_THRESHOLD", "0.9"))
        except:
             sem_threshold = 0.9

        # Optimization: Collect all pairs to encode in batch if we were doing batching.
        # For now, simplistic loop.

        for _, row in df_truth.iterrows():
            term_en = normalize_text(row.get('term_en', ''))
            
            # Filter by word count
            if not term_en:
                 continue
            
            # Simple word count on normalized term
            word_count = len(term_en.split())
            if word_count > args.max_words:
                continue

            truth_trans = row.get(col_name, '')
            
            if pd.isna(truth_trans):
                continue

            truth_trans = str(truth_trans).strip()
            if not truth_trans: continue

            total += 1
            sys_trans = system_translations.get((term_en, sys_lang_code))
            
            if not sys_trans:
                missing += 1
                continue

            # Calculate Lexical Similarity
            lex_sim = calculate_lexical_similarity(sys_trans, truth_trans)
            total_lex_sim += lex_sim

            # Calculate Semantic Similarity
            sem_sim = 0.0
            if semantic_matcher and semantic_matcher.model:
                sem_sim = semantic_matcher.calculate_similarity(sys_trans, truth_trans)
                # Clip to 0-1 just in case
                sem_sim = max(0.0, min(1.0, sem_sim))
            else:
                sem_sim = lex_sim # Fallback
            
            total_sem_sim += sem_sim
            
            # Exact Match Check (using normalization)
            is_exact = normalize_text(sys_trans) == normalize_text(truth_trans)
            if is_exact:
                matches += 1
            
            # Semantic Pass Check
            is_semantic_pass = sem_sim >= sem_threshold
            if is_semantic_pass:
                semantic_passes += 1
                
            # Overall Pass (Exact OR Semantic)
            if is_exact or is_semantic_pass:
                total_passes += 1
            
            if not is_exact:
                mismatch_entry = {
                    "language": sys_lang_code,
                    "term": term_en,
                    "system": sys_trans,
                    "truth": truth_trans,
                    "lex_score": f"{lex_sim:.2f}",
                    "sem_score": f"{sem_sim:.2f}"
                }
                current_lang_mismatches.append(mismatch_entry)
                all_mismatches.append(mismatch_entry)

        denom = total - missing
        accuracy = (matches / total * 100) if total > 0 else 0
        pass_rate = (total_passes / total * 100) if total > 0 else 0
        sem_pass_rate = (semantic_passes / denom * 100) if denom > 0 else 0
        
        avg_lex_sim = (total_lex_sim / denom * 100) if denom > 0 else 0
        avg_sem_sim = (total_sem_sim / denom * 100) if denom > 0 else 0
        
        stats = {
            "Language": sys_lang_code,
            "Total": total,
            "Missing": missing,
            "Exact%": f"{accuracy:.1f}%",
            "Pass%": f"{pass_rate:.1f}%",
            "Lexical%": f"{avg_lex_sim:.1f}%",
            "Semantic%": f"{avg_sem_sim:.1f}%"
        }
        overall_stats.append(stats)
        
        report_lines.append(f"\n## Language: {sys_lang_code.upper()}")
        report_lines.append(f"- **Total**: {total}")
        report_lines.append(f"- **Exact Match**: {matches} ({accuracy:.1f}%)")
        report_lines.append(f"- **Pass Rate (Exact or Semantic >= {sem_threshold})**: {total_passes} ({pass_rate:.1f}%)")
        report_lines.append(f"- **Lexical Similarity**: {avg_lex_sim:.1f}%")
        report_lines.append(f"- **Semantic Similarity**: {avg_sem_sim:.1f}%")
        
        if current_lang_mismatches:
            report_lines.append("\n### worst Semantic Mismatches (< 0.6)")
            report_lines.append("| Term | System | Truth | Sem | Lex |")
            report_lines.append("|---|---|---|---|---|")
            # Sort by SEMANTIC score (lowest first)
            current_lang_mismatches.sort(key=lambda x: float(x['sem_score']))
            bad_mismatches = [m for m in current_lang_mismatches if float(m['sem_score']) < 0.6]
            for m in bad_mismatches[:10]:
                report_lines.append(f"| {m['term']} | {m['system']} | {m['truth']} | {m['sem_score']} | {m['lex_score']} |")

        # --- Corpus Level Metrics (BLEU / COMET) ---
        # We need parallel lists: sys and ref
        # We re-iterate or use what we collected? We didn't collect clean lists.
        # Let's collect them now.
        sys_corpus = []
        ref_corpus = []
        src_corpus = [] # Needed for COMET

        for _, row in df_truth.iterrows():
            term_en = normalize_text(row.get('term_en', ''))
            if not term_en: continue
            if len(term_en.split()) > args.max_words: continue

            truth_trans = row.get(col_name, '')
            if pd.isna(truth_trans): continue
            truth_trans = str(truth_trans).strip()
            if not truth_trans: continue
            
            sys_trans = system_translations.get((term_en, sys_lang_code))
            if sys_trans:
                sys_corpus.append(sys_trans)
                ref_corpus.append(truth_trans)
                src_corpus.append(term_en) # Using normalized EN term as source
        
        if sys_corpus:
            # BLEU
            if bleu_metric:
                # BLEU expects list of strings for sys, and list of list of strings for refs
                formatted_refs = [ref_corpus]
                score = bleu_metric.corpus_score(sys_corpus, formatted_refs)
                print(f"BLEU score for {sys_lang_code}: {score.score:.2f}")
                
                stats["BLEU"] = f"{score.score:.2f}"
                report_lines.append(f"- **BLEU Score**: {score.score:.2f}")
            
            # COMET
            if comet_model:
                print(f"Calculating COMET score for {sys_lang_code} ({len(sys_corpus)} samples)...")
                data = []
                for s, m, r in zip(src_corpus, sys_corpus, ref_corpus):
                    data.append({"src": s, "mt": m, "ref": r})
                
                try:
                    # gpus=0 to force CPU if no GPU, or remove to auto-detect?
                    # default is 1, let's try 0 if we suspect no GPU or just let it default.
                    # The library usually handles it.
                    model_output = comet_model.predict(data, batch_size=8, gpus=0, num_workers=2)
                    system_score = model_output.system_score
                    print(f"COMET score for {sys_lang_code}: {system_score:.4f}")
                    
                    stats["COMET"] = f"{system_score:.4f}"
                    report_lines.append(f"- **COMET Score**: {system_score:.4f}")
                except Exception as e:
                    print(f"Error calculating COMET: {e}")
                    stats["COMET"] = "Error"

    report_lines.insert(5, "\n## Summary")
    summary_df = pd.DataFrame(overall_stats)
    if not summary_df.empty:
        report_lines.insert(6, summary_df.to_markdown(index=False))

    with open(args.output_report, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nReport generated: {args.output_report}")
    print(summary_df.to_string(index=False))

    if args.mismatches_output and all_mismatches:
        mismatches_df = pd.DataFrame(all_mismatches)
        mismatches_df.to_csv(args.mismatches_output, index=False)
        print(f"Mismatches saved to: {args.mismatches_output}")

if __name__ == "__main__":
    main()
