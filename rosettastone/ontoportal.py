
import requests
import json
import logging
import urllib.parse
from typing import Dict, List, Optional, Any

class OntoPortalClient:
    """
    Client for interacting with OntoPortal-based APIs (EcoPortal, AgroPortal, BioPortal, etc.)
    """
    
    def __init__(self, api_key: str, base_url: str = "http://ecoportal.lifewatch.eu:8080"):
        """
        Initialize the OntoPortal client.
        
        Args:
            api_key: API key for authentication
            base_url: Base URL of the OntoPortal instance (default: EcoPortal)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"apikey token={self.api_key}",
            "Accept": "application/json"
        }

    def search_term(self, term: str, ontology: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search for a term in the portal.
        
        Args:
            term: The term to search for
            ontology: Optional specific ontology acronym to search within
            
        Returns:
            List of search results
        """
        endpoint = f"{self.base_url}/search"
        params = {
            "q": term,
            "require_exact_match": "false",
            "include": "prefLabel,definition,synonym"
        }
        
        if ontology:
            params["ontologies"] = ontology
            
        try:
            logging.info(f"Searching OntoPortal for: {term}")
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get("collection", [])
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error searching OntoPortal: {e}")
            return []

    def get_term_details(self, term_uri: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific class/term using its URI.
        Note: OntoPortal usually requires the class URL from its own API, not the original URI.
        However, the search result provides the 'links' -> 'self' URL which works best.
        
        Args:
            term_uri: The API URL for the term (from search results)
            
        Returns:
            Dictionary with detailed term information or None
        """
        try:
            # If it's an external URI, we might need to find the specific ontology class path
            # But typically we use the URL returned by search()
            response = requests.get(term_uri, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error getting term details: {e}")
            return None

    def run_sparql(self, query: str, ontology: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute a SPARQL query against the OntoPortal SPARQL endpoint.
        
        Args:
            query: The SPARQL query string
            ontology: Optional specific ontology to query (might be part of the endpoint or graph)
            
        Returns:
            SPARQL result dictionary (JSON format)
        """
        # Note: EcoPortal SPARQL endpoint is often at /sparql or a specific port
        # We'll assume standard endpoint location, but this might need adjustment based on specific deployment
        endpoint = f"{self.base_url}/sparql"
        
        # Some portals require the ontology to be specified in the FROM clause of the query
        # or via a specific endpoint per ontology.
        
        params = {
            "query": query,
            "format": "json",
            "apikey": self.api_key # Often passed as param for SPARQL
        }
        
        try:
            logging.info("Executing SPARQL query...")
            # Headers for SPARQL might differ slightly
            sparql_headers = self.headers.copy()
            sparql_headers["Accept"] = "application/sparql-results+json"
            
            response = requests.get(endpoint, headers=sparql_headers, params=params)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error executing SPARQL query: {e}")
            return {"error": str(e)}

    def get_definition(self, term: str) -> Optional[str]:
        """
        High-level helper to get the definition of a term.
        Returns the first definition found.
        """
        results = self.search_term(term)
        if not results:
            return None
            
        # Check first result
        first_match = results[0]
        
        # Definitions can be a list or single string
        definitions = first_match.get("definition")
        if definitions:
            if isinstance(definitions, list):
                return definitions[0]
            return str(definitions)
            
        # If not in search summary, try fetching details if we have self link
        links = first_match.get("links", {})
        self_link = links.get("self")
        
        if self_link:
            details = self.get_term_details(self_link)
            if details:
                defs = details.get("definition")
                if defs:
                    return defs[0] if isinstance(defs, list) else str(defs)
                    
    def resolve_uri_via_sparql(self, uri: str, ontology: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Try to resolve a URI (label and definition) using SPARQL.
        Useful when the search API fails for specific URIs.
        
        Args:
            uri: The URI of the concept
            ontology: Optional ontology acronym (used to construct graph URI if needed)
            
        Returns:
            Dictionary with 'label' and 'definition', or None if failed.
        """
        # Construct SPARQL query
        # We try standard SKOS and RDFS properties
        query = f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        
        SELECT ?label ?definition
        WHERE {{
          <{uri}> skos:prefLabel|rdfs:label ?label .
          OPTIONAL {{ <<{uri}> skos:definition|rdfs:comment ?definition }}
        }}
        LIMIT 1
        """
        
        # If specific ontology is known, we might want to restrict GRAPH
        # But usually the default endpoint queries the union graph or handles it.
        
        results = self.run_sparql(query)
        
        if "results" in results and "bindings" in results["results"]:
            bindings = results["results"]["bindings"]
            if bindings:
                first = bindings[0]
                label = first.get("label", {}).get("value")
                definition = first.get("definition", {}).get("value")
                
                if label:
                    return {
                        "label": label,
                        "definition": definition or "No definition found via SPARQL."
                    }
                    
        return None
