import json
import argparse
import sys
import datetime
import os

def generate_croissant_metadata(dataset_name, description, file_path, num_records, source_url=None, source_file=None, llm_model="gpt-oss:latest"):
    """Generates a basic Croissant metadata.json structure."""
    
    current_date = datetime.datetime.now().isoformat()
    
    # Auto-detect models from CSV if possible
    models_found = set(llm_model.split(",")) if llm_model else set()
    import csv
    import os
    
    actual_file_path = file_path
    if not os.path.exists(actual_file_path):
         script_dir = os.path.dirname(os.path.abspath(__file__))
         proj_root = os.path.dirname(os.path.dirname(script_dir))
         try_path = os.path.join(proj_root, file_path)
         if os.path.exists(try_path):
              actual_file_path = try_path

    if os.path.exists(actual_file_path):
        try:
            with open(actual_file_path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if "winning_model" in row and row["winning_model"]:
                        models_found.add(row["winning_model"].strip())
        except:
            pass
    
    # Parse dataset_name if it is a JSON string (for multilingual support)
    name_value = dataset_name
    try:
        name_obj = json.loads(dataset_name)
        if isinstance(name_obj, dict):
             # Legacy dict format: {lang: value}
             name_value = []
             for lang, val in name_obj.items():
                 name_value.append({"@value": val, "@language": lang})
        elif isinstance(name_obj, list):
             # New list format: [{"value": ..., "lang": ..., "model": ...}]
             name_value = []
             for item in name_obj:
                 entry = {"@value": item["value"], "@language": item["lang"]}
                 if item.get("model"):
                      # Link to creator ID
                      entry["creator"] = {"@id": f"model_{item['model'].strip().replace(':', '_').replace('.', '_')}"}
                 name_value.append(entry)
    except:
        pass # Treat as simple string

    metadata = {
        "@context": {
            "@language": "en",
            "@vocab": "https://schema.org/",
            "cr": "http://mlcommons.org/croissant/",
            "rai": "http://mlcommons.org/croissant/RAI/"
        },
        "@type": "sc:Dataset",
        "name": name_value,
        "description": description,
        "datePublished": current_date,
        "creator": [
            {
                "@id": f"model_{m.strip().replace(':', '_').replace('.', '_')}",
                "@type": "sc:SoftwareApplication",
                "name": m.strip(),
                "version": "1.0",
                "description": f"The Large Language Model ({m.strip()}) used to generate translations."
            } for m in sorted(list(models_found)) if m.strip()
        ],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "distribution": [
            {
                "@type": "cr:FileObject",
                "@id": "file_object",
                "name": "multilingual_cv_data",
                "contentUrl": file_path,
                "encodingFormat": "text/csv",
                "sha256": "TODO:CALCULATE_HASH" 
            }
        ],
        "cr:conformance": "http://mlcommons.org/croissant/1.0"
    }

    if source_url:
        metadata["citation"] = source_url

    fields = [
        {"@type": "cr:Field", "@id": "term", "name": "term", "description": "The source term being translated.", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "term"}}},
        {"@type": "cr:Field", "@id": "context", "name": "context", "description": "The definition or context of the term.", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "context"}}},
        {"@type": "cr:Field", "@id": "translation", "name": "translation", "description": "The translated term.", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "translation"}}},
        {"@type": "cr:Field", "@id": "language", "name": "language", "description": "The ISO 639-1 language code of the translation.", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "language"}}},
        {"@type": "cr:Field", "@id": "confidence", "name": "confidence", "description": "The confidence score of the translation (0.0 to 1.0).", "dataType": "sc:Float", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "confidence"}}},
        {"@type": "cr:Field", "@id": "winning_model", "name": "winning_model", "description": "The software agent selected as the source for this translation row.", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "winning_model"}}},
        {"@type": "cr:Field", "@id": "consensus", "name": "consensus", "description": "The decision reached by the arbitrage logic (e.g., consensus reached and vote count).", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "consensus"}}},
        {"@type": "cr:Field", "@id": "version", "name": "version", "description": "The version of the software used.", "dataType": "sc:Text", "source": {"fileObject": {"@id": "file_object"}, "extract": {"column": "version"}}}
    ]
    
    metadata["recordSet"] = [
            {
                "@type": "cr:RecordSet",
                "@id": "record_set",
                "name": "translations",
                "field": fields
            }
        ]
    
    return metadata

def main():
    parser = argparse.ArgumentParser(description="Generate Croissant Metadata for Multilingual CV")
    parser.add_argument("--output-dir", "--output_dir", dest="output_dir", default=".", help="Directory to save the metadata file")
    parser.add_argument("--output-file", "--output_file", dest="output_file", default="metadata.json", help="Filename for the metadata (default: metadata.json)")
    parser.add_argument("--data-file", "--data_file", dest="data_file", required=True, help="Path to the final CSV data file (relative to output_dir)")
    parser.add_argument("--dataset-name", "--dataset_name", dest="dataset_name", default="Multilingual Controlled Vocabulary", help="Name of the dataset")
    parser.add_argument("--description", default="A multilingual controlled vocabulary dataset generated by Gemini 3 agents.", help="Description of the dataset")
    parser.add_argument("--source-url", "--source_url", dest="source_url", help="URL source of the original term")
    parser.add_argument("--source-file", "--source_file", dest="source_file", help="File source of the original term")
    parser.add_argument("--llm-model", "--llm_model", dest="llm_model", default="gpt-oss:latest", help="The LLM model used for generation")
    
    # In a real pipeline, we might accept a JSON blob of results to append to the CSV, 
    # but for now we'll assume the data file is being managed or passed in.
    
    args = parser.parse_args()
    
    # Placeholder for reading line count or calculating hash
    num_records = 0 # would calculate normally
    
    metadata = generate_croissant_metadata(
        args.dataset_name, 
        args.description,
        args.data_file,
        num_records,
        source_url=args.source_url,
        source_file=args.source_file,
        llm_model=args.llm_model
    )
    
    output_path = os.path.join(args.output_dir, args.output_file)
    with open(output_path, "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    main()
