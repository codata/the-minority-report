
import os
import sys
import json
import re
import argparse
import requests
import glob
from converter import croissant_to_dataverse

def ingest_dataverse(input_dir, dataverse_url, dataverse_id, api_token, input_file=None, config=None):
    """
    Ingests Croissant metadata files into Dataverse.
    """
    if input_file:
        if not os.path.exists(input_file):
             print(f"Error: Input file {input_file} does not exist.")
             sys.exit(1)
        files = [input_file]
    else:
        if not os.path.isdir(input_dir):
            print(f"Error: Input directory {input_dir} does not exist.")
            sys.exit(1)
        files = glob.glob(os.path.join(input_dir, "croissant_*.json"))
        
    # Normalize URL
    dataverse_url = dataverse_url.rstrip('/')
    
    # API Endpoint
    api_endpoint = f"{dataverse_url}/api/dataverses/{dataverse_id}/datasets"
    
    headers = {
        "X-Dataverse-key": api_token,
        "Content-Type": "application/ld+json"
    }

    if not files:
        print(f"No metadata files found.")
        return

    print(f"Found {len(files)} metadata file(s) to ingest...")

    for file_path in files:
        print(f"\nProcessing {file_path}...")
        try:
            with open(file_path, 'r') as f:
                croissant_data = json.load(f)
            
            # Fetch Wikidata Link from SparqlMuse EARLY to use in metadata
            sparqlmuse_api_url = config.get("sparqlmuse_api") if config else None
            wikilink_url = None
            wikilink_json = None
            
            if sparqlmuse_api_url:
                term_name = croissant_data.get("name")
                description = croissant_data.get("description", "")
                
                if term_name:
                    import urllib.parse
                    params = {
                        "term": term_name,
                        "context": description[:500],
                        "language": "en",
                        "format": "json"
                    }
                    query_string = urllib.parse.urlencode(params)
                    full_url = f"{sparqlmuse_api_url}?{query_string}"
                    
                    try:
                        print(f"\nFetching Wikidata link from SparqlMuse: {full_url}")
                        wikilink_resp = requests.get(full_url)
                        
                        if wikilink_resp.status_code == 200:
                            wikilink_str = wikilink_resp.text
                            try:
                                wikilink_data = json.loads(wikilink_str)
                                wikilink_url = wikilink_data.get("url")
                                wikilink_json = wikilink_str # Keep for file upload later
                                if wikilink_url:
                                    print(f"Propagating Wikidata URI: {wikilink_url}")
                            except ValueError:
                                print("Invalid JSON from SparqlMuse")
                    except Exception as e:
                        print(f"Error handling SparqlMuse fetch: {e}")

            # Update config with fetched URI if available
            current_config = config.copy() if config else {}
            if wikilink_url:
                current_config['keyword_vocabulary_uri'] = wikilink_url

            # Convert
            dv_data = croissant_to_dataverse(croissant_data, current_config)
            
            # Upload Metadata to Create Dataset
            print(f"Creating dataset at {api_endpoint}...")
            response = requests.post(api_endpoint, data=json.dumps(dv_data), headers=headers)
            
            if response.status_code == 201:
                persistent_id = response.json().get('data', {}).get('persistentId')
                print(f"Success! Created dataset: {persistent_id}")
                
                # Initialize API
                from pyDataverse.api import NativeApi
                api = NativeApi(dataverse_url, api_token)
                
                # 1. Upload SKOS (Enrichment)
                cite_as = croissant_data.get("citeAs", "")
                hips_match = re.search(r'(MH\d+)', cite_as, re.IGNORECASE)
                if hips_match:
                    hips_code = hips_match.group(1).upper()
                    print(f"\nFound HIPS Code: {hips_code}")
                    hips_api_url = f"https://www.undrr.org/api/terms/hips/{hips_code}"
                    
                    try:
                        print(f"Fetching SKOS from {hips_api_url}...")
                        skos_resp = requests.get(hips_api_url)
                        
                        if skos_resp.status_code == 200:
                            safe_name = croissant_data.get("name", "hazard").lower().replace(" ", "_").replace("/", "_")
                            skos_filename = f"skos_{safe_name}.json"
                            
                            with open(skos_filename, 'w') as skos_f:
                                skos_f.write(skos_resp.text)
                                
                            print(f"Uploading {skos_filename}...")
                            skos_upload = api.upload_datafile(persistent_id, skos_filename, json.dumps({"description": f"SKOS data for {hips_code}", "categories": ["Data"]}))
                            
                            if skos_upload.status_code == 200:
                                print(f"SKOS upload successful.")
                            else:
                                print(f"SKOS upload failed: {skos_upload.status_code}")

                            if os.path.exists(skos_filename):
                                os.remove(skos_filename)
                    except Exception as e:
                        print(f"Error handling SKOS: {e}")

                # 2. Upload Wikilink (Enrichment)
                if wikilink_json and term_name:
                    safe_name = croissant_data.get("name", "hazard").lower().replace(" ", "_").replace("/", "_")
                    wikilink_filename = f"wikilink_{safe_name}.json"
                    try:
                        with open(wikilink_filename, 'w') as wl_f:
                            wl_f.write(wikilink_json)
                            
                        print(f"Uploading {wikilink_filename}...")
                        wl_upload = api.upload_datafile(persistent_id, wikilink_filename, json.dumps({"description": f"Wikidata Link for {term_name}", "categories": ["Data"]}))
                        
                        if wl_upload.status_code == 200:
                            print(f"Wikilink upload successful.")
                        else:
                            print(f"Wikilink upload failed: {wl_upload.status_code}")
                            
                        if os.path.exists(wikilink_filename):
                            os.remove(wikilink_filename)
                    except Exception as e:
                        print(f"Error uploading Wikilink file: {e}")

                # 3. Upload Translations CSV and Capture ID
                translations_url = None
                translations_csv_path = config.get("translations_csv") if config else None
                if translations_csv_path and os.path.exists(translations_csv_path):
                    term_name = croissant_data.get("name")
                    if term_name:
                        import csv
                        safe_name = croissant_data.get("name", "hazard").lower().replace(" ", "_").replace("/", "_")
                        translations_out_file = f"translations_{safe_name}.csv"
                        found_translations = False
                        
                        try:
                            with open(translations_csv_path, 'r', encoding='utf-8') as csv_in, \
                                 open(translations_out_file, 'w', encoding='utf-8', newline='') as csv_out:
                                
                                reader = csv.DictReader(csv_in)
                                writer = csv.DictWriter(csv_out, fieldnames=reader.fieldnames)
                                writer.writeheader()
                                
                                for row in reader:
                                    if row.get('term') == term_name:
                                        writer.writerow(row)
                                        found_translations = True
                            
                            if found_translations:
                                print(f"Found translations for '{term_name}', uploading {translations_out_file}...")
                                trans_upload = api.upload_datafile(persistent_id, translations_out_file, json.dumps({"description": f"Translations for {term_name}", "categories": ["Data"]}))
                                
                                if trans_upload.status_code == 200:
                                    print(f"Translations upload successful.")
                                    try:
                                        file_data = trans_upload.json()['data']['files'][0]['dataFile']
                                        file_id = file_data['id']
                                        translations_url = f"{dataverse_url}/api/access/datafile/{file_id}"
                                        print(f"Captured Translations URL: {translations_url}")
                                    except Exception as e:
                                        print(f"Could not extract file ID: {e}")
                                else:
                                    print(f"Translations upload failed: {trans_upload.status_code} {trans_upload.text}")
                            else:
                                print(f"No translations found for '{term_name}' in {translations_csv_path}")

                            # Cleanup
                            if os.path.exists(translations_out_file):
                                os.remove(translations_out_file)

                        except Exception as e:
                            print(f"Error processing translations CSV: {e}")

                # Upload SparqlMuse Wikidata Link
                if wikilink_json and term_name:
                    wikilink_filename = f"wikilink_{safe_name}.json"
                    try:
                        with open(wikilink_filename, 'w') as wl_f:
                            wl_f.write(wikilink_json)
                            
                        print(f"Uploading {wikilink_filename}...")
                        wl_upload = api.upload_datafile(persistent_id, wikilink_filename, json.dumps({"description": f"Wikidata Link for {term_name}", "categories": ["Data"]}))
                        
                        if wl_upload.status_code == 200:
                            print(f"Wikilink upload successful.")
                        else:
                            print(f"Wikilink upload failed: {wl_upload.status_code} {wl_upload.text}")
                            
                        # Cleanup
                        if os.path.exists(wikilink_filename):
                            os.remove(wikilink_filename)
                            
                    except Exception as e:
                        print(f"Error uploading Wikilink file: {e}")

                # 4. Modify Croissant Data & Upload
                if translations_url:
                    print("Updating Croissant metadata with translations URL...")
                    # Find FileObject named 'multilingual_cv_data'
                    # It might be in distribution list
                    distributions = croissant_data.get('distribution', [])
                    updated = False
                    for dist in distributions:
                        if dist.get('@type') == 'cr:FileObject' and dist.get('name') == 'multilingual_cv_data':
                            dist['contentUrl'] = translations_url
                            dist['sha256'] = "" # Reset hash as content is now remote/dynamic
                            updated = True
                            print("Updated contentUrl for multilingual_cv_data")
                    
                    if not updated:
                         print("Warning: Could not find 'multilingual_cv_data' FileObject to update.")
                
                # Save modified JSON
                safe_name = croissant_data.get("name", "hazard").lower().replace(" ", "_").replace("/", "_")
                final_croissant_file = f"croissant_{safe_name}_final.json"
                with open(final_croissant_file, 'w') as f:
                    json.dump(croissant_data, f, indent=2)
                
                print(f"Uploading final Croissant file {final_croissant_file}...")
                try:
                    df = api.upload_datafile(persistent_id, final_croissant_file, json.dumps({"description": "Croissant Metadata", "categories": ["Metadata"]}))
                    if df.status_code == 200:
                        print(f"Croissant file upload successful.")
                    else:
                        print(f"Croissant file upload failed: {df.status_code} {df.text}")
                except Exception as e:
                    print(f"Croissant upload exception: {e}")
                    
                if os.path.exists(final_croissant_file):
                    os.remove(final_croissant_file)
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Croissant metadata into Dataverse.")
    parser.add_argument("--input-dir", default="output", help="Directory containing croissant_*.json files")
    parser.add_argument("--file", help="Path to a single Croissant JSON file to ingest (overrides --input-dir)")
    parser.add_argument("--dataverse-url", default=os.environ.get("DATAVERSE_URL"), help="Dataverse base URL")
    parser.add_argument("--dataverse-id", default=os.environ.get("DATAVERSE_ID"), help="Target Dataverse collection alias or ID")
    parser.add_argument("--api-token", default=os.environ.get("DATAVERSE_API_TOKEN"), help="Dataverse API Token")
    parser.add_argument("--config", default="dataverse/ingest.conf", help="Path to configuration file")

    args = parser.parse_args()

    if not args.dataverse_url or not args.dataverse_id or not args.api_token:
        print("Error: Missing Dataverse configuration. Please provide --dataverse-url, --dataverse-id, and --api-token (or set env vars).")
        sys.exit(1)

    config_data = None
    if args.config:
        try:
            with open(args.config, 'r') as f:
                config_data = json.load(f)
        except Exception as e:
            print(f"Warning: Could not load config file {args.config}: {e}")
            print("Using default values.")

    ingest_dataverse(args.input_dir, args.dataverse_url, args.dataverse_id, args.api_token, args.file, config_data)
