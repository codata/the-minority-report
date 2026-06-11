import os
from rdflib import Graph

def read_policy():
    # Attempt to load from the environment variable, or use a relative fallback
    policy_path = os.environ.get("ODRL_POLICY_PATH")
    
    # Resolve the path dynamically if it's not explicitly set in env
    if not policy_path or not os.path.exists(policy_path):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        policy_path = os.path.join(base_dir, "ODRL", "translation_pipeline_odrl.jsonld")
        
        if not os.path.exists(policy_path):
            print(f"Error: Policy file not found at {policy_path}")
            return

    print(f"Loading ODRL Policy from: {policy_path}\n")
    
    # Initialize the RDF Graph
    g = Graph()
    
    try:
        # Parse the JSON-LD file
        g.parse(policy_path, format="json-ld")
        print(f"Successfully parsed {len(g)} RDF triples from the policy.\n")
        
        print("=========================================")
        print("  ODRL Policy representation (Turtle)")
        print("=========================================")
        # Turtle is a highly readable format for RDF data
        print(g.serialize(format="turtle"))
        
        print("\n=========================================")
        print("  Extracted Triples (Subject, Predicate, Object)")
        print("=========================================")
        # Iterate over and print all raw triples
        for count, (s, p, o) in enumerate(g, 1):
            print(f"Triple {count}:")
            print(f"  Subject:   {s}")
            print(f"  Predicate: {p}")
            print(f"  Object:    {o}")
            print("-" * 40)
            
    except Exception as e:
        print(f"Failed to parse ODRL Policy: {e}")

if __name__ == "__main__":
    read_policy()
