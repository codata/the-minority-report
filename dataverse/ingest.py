
import os
import sys
import json
import argparse
import requests
import glob
from converter import croissant_to_dataverse

def ingest_dataverse(input_dir, dataverse_url, dataverse_id, api_token):
    """
    Ingests Croissant metadata files from input_dir into Dataverse.
    """
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory {input_dir} does not exist.")
        sys.exit(1)

    # Normalize URL
    dataverse_url = dataverse_url.rstrip('/')
    
    # API Endpoint
    api_endpoint = f"{dataverse_url}/api/dataverses/{dataverse_id}/datasets"
    
    headers = {
        "X-Dataverse-key": api_token,
        "Content-Type": "application/ld+json"
    }

    files = glob.glob(os.path.join(input_dir, "croissant_*.json"))
    if not files:
        print(f"No croissant_*.json files found in {input_dir}")
        return

    print(f"Found {len(files)} metadata files to ingest...")

    for file_path in files:
        print(f"\nProcessing {file_path}...")
        try:
            with open(file_path, 'r') as f:
                croissant_data = json.load(f)
            
            # Convert
            dv_data = croissant_to_dataverse(croissant_data)
            
            # Upload
            print(f"Uploading to {api_endpoint}...")
            response = requests.post(api_endpoint, data=json.dumps(dv_data), headers=headers)
            
            if response.status_code == 201:
                print(f"Success! Created dataset: {response.json().get('data', {}).get('persistentId')}")
            else:
                print(f"Failed with status {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Croissant metadata into Dataverse.")
    parser.add_argument("--input-dir", default="output", help="Directory containing croissant_*.json files")
    parser.add_argument("--dataverse-url", default=os.environ.get("DATAVERSE_URL"), help="Dataverse base URL")
    parser.add_argument("--dataverse-id", default=os.environ.get("DATAVERSE_ID"), help="Target Dataverse collection alias or ID")
    parser.add_argument("--api-token", default=os.environ.get("DATAVERSE_API_TOKEN"), help="Dataverse API Token")

    args = parser.parse_args()

    if not args.dataverse_url or not args.dataverse_id or not args.api_token:
        print("Error: Missing Dataverse configuration. Please provide --dataverse-url, --dataverse-id, and --api-token (or set env vars).")
        sys.exit(1)

    ingest_dataverse(args.input_dir, args.dataverse_url, args.dataverse_id, args.api_token)
