import sys
import os

# Adjust path to import mcp_server
sys.path.append(os.path.abspath("translation-skill/scripts"))

from mcp_server import _find_hazards_logic

# Test queries
queries = [
    "Flooding",
    "The disaster risk term in English for Flooding and translation in French (fr) is inondation .",
    "There was a massive flood in the coastal region.",
    "Talvi yllätti Lontoon – arktinen räjähdys pakotti koulut sulkemaan ovensa. Lumimyrsky on laittanut Englannissa pakan sekaisin."
]

for q in queries:
    print(f"\nQuery: {q}")
    try:
        result = _find_hazards_logic(q)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
