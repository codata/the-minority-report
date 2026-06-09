import os
import sys
import argparse
import glob
import json
import re

from orchestrator import mock_llm_call, load_prompt

def extract_json_from_text(text):
    # Try finding <json> block
    match = re.search(r'<json>\s*(.*?)\s*</json>', text, re.DOTALL | re.IGNORECASE)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
            
    # Fallback to general markdown JSON extraction
    match = re.search(r'```(?:json)?\s*(.*?)\s*```', text, re.DOTALL | re.IGNORECASE)
    if match:
         try:
             return json.loads(match.group(1))
         except json.JSONDecodeError:
             pass
    
    # Fallback to brute force first { and last }
    try:
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1:
            return json.loads(text[start:end+1])
    except:
        pass
        
    return {"variables": [], "indicators": [], "risk_drivers": []}

def process_file(md_path, prompt_template, model):
    print(f"Processing {md_path}...")
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Determine language from directory name
    lang_code = os.path.basename(os.path.dirname(md_path))
    target_lang = lang_code if lang_code else "en"

    prompt = prompt_template.replace("{{text}}", text).replace("{{language}}", target_lang)
    
    # We pass is_json=False because the model is expected to return a <chain_of_thought> before the JSON
    response_text = mock_llm_call(prompt, model=model, is_json=False)
    
    data = extract_json_from_text(response_text)

    # md_path is like .../hips/MH0705/translations/ru/MH0705_article.md
    dirname = os.path.dirname(md_path)
    lang = os.path.basename(dirname)
    translations_dir = os.path.dirname(dirname)
    hips_dir = os.path.dirname(translations_dir)
    
    cdif_dir = os.path.join(hips_dir, "CDIF", lang)
    os.makedirs(cdif_dir, exist_ok=True)
    
    basename = os.path.basename(md_path)
    name_without_ext = os.path.splitext(basename)[0]
    out_path = os.path.join(cdif_dir, f"{name_without_ext}_metrics.json")
    
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"  Saved metrics to {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract variables and indicators from translated markdown files.")
    parser.add_argument("--hips-code", help="Process only a specific HIPS code. If omitted, processes all.", default=None)
    parser.add_argument("--language", help="Process only a specific language (e.g. 'ru'). If omitted, processes all.", default=None)
    parser.add_argument("--model", help="Model to use for extraction.", default="gpt-oss:latest")
    parser.add_argument("--prompts-dir", help="Directory containing prompt templates", default="translation-skill/prompts")
    args = parser.parse_args()

    # Load prompt from same relative dir if running locally, or using passed arg
    # Adjust default prompts_dir based on script location if needed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if args.prompts_dir == "translation-skill/prompts":
        # Check if we are running from root or from scripts/
        if os.path.exists(os.path.join(script_dir, "..", "prompts", "metrics_extraction_prompt.md")):
            prompts_dir = os.path.join(script_dir, "..", "prompts")
        else:
            prompts_dir = args.prompts_dir
    else:
        prompts_dir = args.prompts_dir

    prompt_path = os.path.join(prompts_dir, "metrics_extraction_prompt.md")
    if not os.path.isfile(prompt_path):
        print(f"Error: Prompt file not found at {prompt_path}")
        sys.exit(1)
        
    prompt_template = load_prompt(prompt_path)

    base_dir = os.path.join(script_dir, "..", "..", "hips")
    
    search_code = args.hips_code if args.hips_code else "*"
    search_lang = args.language if args.language else "*"
    
    pattern = os.path.join(base_dir, search_code, "translations", search_lang, "*.md")
    md_files = glob.glob(pattern)
    
    if not md_files:
        print(f"No translated markdown files found matching pattern: {pattern}")
        sys.exit(0)
        
    print(f"Found {len(md_files)} markdown files to process.")
    for md_path in md_files:
        process_file(md_path, prompt_template, args.model)

if __name__ == "__main__":
    main()
