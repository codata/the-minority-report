import json
import argparse
import sys
import datetime
import os
import csv
from rdflib import Graph, Namespace, RDFS
from rdflib.namespace import SKOS
import mlcroissant as mlc

def load_semantic_mappings(mapping_file):
    """
    Loads the Turtle mapping file and returns a dictionary mapping
    CSV columns (local namespace) to a dict of {target: URI, description: str}.
    """
    g = Graph()
    g.parse(mapping_file, format="turtle")
    
    # We want a map: CSV_Column_Name -> {target: Target_Property_URI, description: Comment}
    mappings = {}
    
    # Query the graph for exact matches
    # ?localColumn skos:exactMatch ?targetProperty
    for s, p, o in g.triples((None, SKOS.exactMatch, None)):
        local_name = s.split("/")[-1]
        target_uri = str(o)
        
        # Get description (rdfs:comment)
        description = None
        for _, _, comment in g.triples((s, RDFS.comment, None)):
            description = str(comment)
            break
            
        mappings[local_name] = {
            "target_uri": target_uri,
            "description": description
        }
        
    return mappings

def generate_croissant_metadata(dataset_name, description, file_path, num_records, source_url=None, source_file=None, llm_model="gpt-oss:latest", mapping_file=None, hips_code=None):
    """Generates a Croissant metadata structure using mlcroissant library."""
    
    # Load Mappings
    if not mapping_file:
         script_dir = os.path.dirname(os.path.abspath(__file__))
         mapping_file = os.path.join(os.path.dirname(script_dir), "mappings", "csv_to_croissant.ttl")
    
    column_map = {}
    if os.path.exists(mapping_file):
        try:
             column_map = load_semantic_mappings(mapping_file)
             print(f"Loaded semantic mappings from {mapping_file}")
        except Exception as e:
             print(f"Error loading semantic mappings: {e}")
    else:
        print(f"Warning: Mapping file {mapping_file} not found. Using defaults.")

    # Auto-detect models
    models_found = set(llm_model.split(",")) if llm_model else set()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if "winning_model" in row and row["winning_model"]:
                        models_found.add(row["winning_model"].strip())
        except:
            pass

    # Build Creators List
    creators = []
    for m in sorted(list(models_found)):
        if m.strip():
            # Note: mlcroissant doesn't have a direct 'SoftwareApplication' type helper yet roughly, 
            # so we might pass these as simple dicts or objects if allowed. 
            # mlc.Metadata.creators expects a list of Person or Organization usually? 
            # Looking at the library, it might support dictionary for custom types.
            # Let's try passing dict with @type for now, or check if mlc has classes.
            # If not, we can pass standard json-ld dicts.
            creators.append({
                "@type": "sc:SoftwareApplication",
                "@id": f"model_{m.strip().replace(':', '_').replace('.', '_')}",
                "name": m.strip(),
                "version": "1.0",
                "description": f"The Large Language Model ({m.strip()}) used to generate translations."
            })

    # Define FileObject
    distribution = [
        mlc.FileObject(
            id="file_object",
            name="multilingual_cv_data",
            content_url=file_path,
            encoding_format="text/csv",
            sha256="TODO:CALCULATE_HASH" 
        )
    ]
    
    # Dynamic Field Generation
    known_columns = ["term", "context", "translation", "language", "confidence", "winning_model", "consensus", "version"]
    fields = []
    
    for col in known_columns:
        mapping_info = column_map.get(col, {})
        # mapping_info is now {target_uri: ..., description: ...} or empty
        
        # Use description from mapping, fall back to empty string
        desc = mapping_info.get("description", "")
        
        # If no description in mapping, fall back to defaults (optional, but good for safety)
        if not desc:
            if col == "term": desc = "The source term being translated."
            if col == "context": desc = "The definition or context of the term."
            if col == "translation": desc = "The translated term."
            if col == "language": desc = "The ISO 639-1 language code of the translation."
            if col == "confidence": desc = "The confidence score of the translation (0.0 to 1.0)."
            if col == "winning_model": desc = "The software agent selected as the source for this translation row."
            if col == "consensus": desc = "The decision reached by the arbitrage logic (e.g., consensus reached and vote count)."
            if col == "version": desc = "The version of the software used."
        
        dtype = mlc.DataType.FLOAT if col == "confidence" else mlc.DataType.TEXT
        
        fields.append(
            mlc.Field(
                id=col,
                name=col,
                description=desc,
                data_types=[dtype],
                source=mlc.Source(
                    file_object="file_object",
                    extract=mlc.Extract(column=col)
                )
            )
        )

    # Define RecordSet
    record_sets = [
        mlc.RecordSet(
            id="record_set",
            name="translations",
            fields=fields
        )
    ]

    # Construct Metadata
    # Fix: mlcroissant expects name to be a string. 
    # We extract the English name or first available value as the main name.
    final_name = "Multilingual Dataset"
    try:
        if isinstance(dataset_name, str):
            # Try parsing if it looks like JSON
            if dataset_name.strip().startswith("[") or dataset_name.strip().startswith("{"):
                try:
                    name_obj = json.loads(dataset_name)
                except:
                    name_obj = dataset_name
            else:
                name_obj = dataset_name
        else:
             name_obj = dataset_name
             
        if isinstance(name_obj, list):
            # Find en
            for item in name_obj:
                if item.get("lang") == "en" or item.get("@language") == "en":
                     final_name = item.get("value") or item.get("@value")
                     break
            else:
                # Use first
                if len(name_obj) > 0:
                    item = name_obj[0]
                    final_name = item.get("value") or item.get("@value")
    except:
        final_name = str(dataset_name)

    # Parse multilingual name for jsonld injection
    extra_jsonld = {}
    
    # Inject HIPS Code if provided
    if hips_code:
        # Using schema:identifier
        # https://schema.org/identifier
        extra_jsonld["https://schema.org/identifier"] = hips_code

    if isinstance(name_obj, list):
         # Schema.org expects Text or TextObject. 
         # We can pass the list of dicts directly if keys match JSON-LD compaction (value/language -> @value/@language)
         # The input name_obj has keys "value", "lang" or "@value", "@language" depending on source.
         # We normalize to JSON-LD standard.
         normalized_names = []
         for item in name_obj:
             val = item.get("value") or item.get("@value")
             lang = item.get("lang") or item.get("@language")
             model = item.get("model") or item.get("creator") 
             # If creator is dict, extract @id or name
             if isinstance(model, dict):
                 model = model.get("@id") or model.get("name")
                 
             if val and lang:
                 entry = {
                     "@value": val,
                     "@language": lang
                 }
                 if model:
                      # If just model name, make it a reference
                      if not model.startswith("model_"):
                           model_id = f"model_{model.strip().replace(':', '_').replace('.', '_')}"
                      else:
                           model_id = model
                      
                      entry["creator"] = {"@id": model_id}
                      
                 normalized_names.append(entry)
         
         if normalized_names:
             extra_jsonld["https://schema.org/alternateName"] = normalized_names

    # Use source_url as citation if available
    cite_as = source_url if source_url else None

    metadata = mlc.Metadata(
        name=final_name,
        description=description,
        date_published=datetime.datetime.now(), # Pass object, let serializer handle or to_json
        creators=creators,
        license="https://creativecommons.org/licenses/by/4.0/",
        distribution=distribution,
        record_sets=record_sets,
        version="1.0.0",
        cite_as=cite_as,
        jsonld=extra_jsonld
    )
    
    
    # Validation happens on init/post_init usually
    json_output = metadata.to_json()

    # Manual injection of alternateName if available
    # mlcroissant might not handle custom jsonld injection as expected for top-level metadata
    if extra_jsonld.get("https://schema.org/alternateName"):
        # Check context for alias
        # We assume standard context where sc -> https://schema.org/
        # or vocab is schema.org
        json_output["sc:alternateName"] = extra_jsonld["https://schema.org/alternateName"]

    if extra_jsonld.get("https://schema.org/identifier"):
        json_output["https://schema.org/identifier"] = extra_jsonld["https://schema.org/identifier"]

    # Restore citeAs if lost during serialization
    if cite_as and "citeAs" not in json_output:
         json_output["citeAs"] = cite_as
         
    return json_output

# Helper for datetime serialization
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super().default(o)

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
    parser.add_argument("--mapping-file", "--mapping_file", dest="mapping_file", help="Path to Turtle mapping file")
    parser.add_argument("--hips-code", "--hips_code", dest="hips_code", help="HIPS ID (e.g., BI0310) to append to branding")

    args = parser.parse_args()
    
    # Generate
    try:
        # Prepare HIPS code injection via JSON-LD if present
        extra_jsonld = {}
        if args.hips_code:
            # Inject as schema:identifier
            # We can pass this into generate_croissant_metadata or modify logic there.
            # But generate_croissant_metadata constructs metadata.
            # Let's pass it as a kwarg or modify generate_croissant_metadata signature?
            # Actually, let's just modifying generate_croissant_metadata to accept it, 
            # Or pass it via description? No, user wants separate field.
            # Best way: Pass it to function.
            pass

        json_output = generate_croissant_metadata(
            args.dataset_name, 
            args.description,
            args.data_file,
            0,
            source_url=args.source_url,
            source_file=args.source_file,
            llm_model=args.llm_model,
            mapping_file=args.mapping_file,
            hips_code=args.hips_code 
        )
        
        output_path = os.path.join(args.output_dir, args.output_file)
        with open(output_path, "w") as f:
            json.dump(json_output, f, indent=2, cls=DateTimeEncoder)
        
        print(f"Successfully generated {output_path}")
        
    except Exception as e:
        print(f"Error generating Croissant metadata: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
