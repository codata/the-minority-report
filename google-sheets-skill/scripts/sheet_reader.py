import pandas as pd
import re

def get_google_sheet_csv_url(url):
    """
    Converts a standard Google Sheet URL to a CSV export URL.
    """
    # Extract Sheet ID
    # Pattern: /d/([a-zA-Z0-9-_]+)
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
    if not match:
        raise ValueError("Invalid Google Sheet URL: Could not extract Sheet ID.")
    
    sheet_id = match.group(1)
    
    # Extract GID if present
    # Pattern: gid=([0-9]+)
    gid = "0" # Default to first sheet
    match_gid = re.search(r'[#&?]gid=([0-9]+)', url)
    if match_gid:
        gid = match_gid.group(1)
        
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

def read_google_sheet(url):
    """
    Reads a Google Sheet and returns a list of dictionaries.
    Expects columns 'term_en' and 'definition_en'.
    Standardizes output to 'term' and 'context'.
    """
    csv_url = get_google_sheet_csv_url(url)
    
    try:
        df = pd.read_csv(csv_url)
        
        # Check required columns
        required_cols = ['term_en', 'definition_en']
        if not all(col in df.columns for col in required_cols):
             # Try fallback to 'term' and 'context' or 'definition'
             term_col = next((c for c in df.columns if c.lower() in ['term', 'term_en', 'concept']), None)
             def_col = next((c for c in df.columns if c.lower() in ['definition', 'definition_en', 'context', 'description']), None)
             
             if not term_col or not def_col:
                 raise ValueError(f"Google Sheet must contain 'term_en' and 'definition_en' columns. Found: {list(df.columns)}")
             
             df = df.rename(columns={term_col: 'term_en', def_col: 'definition_en'})
        
        # Normalize to internal schema
        rows = []
        for _, row in df.iterrows():
            if pd.notna(row['term_en']) and str(row['term_en']).strip():
                rows.append({
                    "term": str(row['term_en']).strip(),
                    "context": str(row['definition_en']).strip() if pd.notna(row['definition_en']) else f"Standard definition for {row['term_en']}",
                    "url": url
                })
                
        return rows
        
    except Exception as e:
        print(f"Error reading Google Sheet: {e}")
        return []

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Read Google Sheet terms")
    parser.add_argument("url", help="Google Sheet URL")
    args = parser.parse_args()
    
    data = read_google_sheet(args.url)
    print(f"Loaded {len(data)} rows.")
    if data:
        print(data[0])
