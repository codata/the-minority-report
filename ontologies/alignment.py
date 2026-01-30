import pandas as pd
import json
import os
import re
import argparse
import requests
import torch
import uuid
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_distances

# Optional Vector DB Imports
try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    chromadb = None

try:
    from qdrant_client import QdrantClient
    from qdrant_client.http.models import Distance, VectorParams, PointStruct
except ImportError:
    QdrantClient = None

class VectorStore:
    def __init__(self, store_type="chroma", collection_name="hips_alignment", qdrant_host="localhost", qdrant_port=6333):
        self.store_type = store_type
        self.collection_name = collection_name
        self.client = None
        self.collection = None
        
        if store_type == "chroma":
            if not chromadb:
                raise ImportError("chromadb not installed run `pip install chromadb`")
            # Persistent client in output directory
            self.client = chromadb.PersistentClient(path="output/chroma_db")
            self.collection = self.client.get_or_create_collection(name=collection_name)
            print(f"[VectorStore] Initialized ChromaDB in output/chroma_db (Collection: {collection_name})")
            
        elif store_type == "qdrant":
            if not QdrantClient:
                raise ImportError("qdrant-client not installed run `pip install qdrant-client`")
            
            self.client = QdrantClient(host=qdrant_host, port=qdrant_port)
            
            # Check if collection exists, if not create
            try:
                self.client.get_collection(collection_name)
            except:
                print(f"[VectorStore] Creating Qdrant collection: {collection_name}")
                self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(size=384, distance=Distance.COSINE), # Assuming MiniLM-L6-v2 size=384
                )
            print(f"[VectorStore] Initialized Qdrant at {qdrant_host}:{qdrant_port} (Collection: {collection_name})")
            
        elif store_type == "file":
             self.file_path = f"output/{collection_name}"
             if not os.path.exists(self.file_path):
                 os.makedirs(self.file_path)
             print(f"[VectorStore] Initialized File Storage in {self.file_path}")

    def add(self, id, text, embedding, metadata):
        if self.store_type == "chroma":
            self.collection.upsert(
                ids=[id],
                documents=[text],
                embeddings=[embedding],
                metadatas=[metadata]
            )
        elif self.store_type == "qdrant":
            self.client.upsert(
                collection_name=self.collection_name,
                points=[
                    PointStruct(
                        id=str(uuid.uuid5(uuid.NAMESPACE_DNS, id)), # Qdrant prefers UUIDs or ints
                        vector=embedding,
                        payload={**metadata, "text": text, "original_id": id}
                    )
                ]
            )
        elif self.store_type == "file":
            # Sanitize filename
            safe_id = re.sub(r'[^a-zA-Z0-9_\-]', '_', id)
            record = {
                "id": id,
                "text": text,
                "embedding": embedding,
                "metadata": metadata
            }
            with open(f"{self.file_path}/{safe_id}.json", "w") as f:
                json.dump(record, f, indent=2)

class CosineDistance:
    def __init__(self, query, model, debug=False, sparqlmuse_host="https://sparqlmuse.now.museum"):
        self.query = query
        self.DEBUG = debug
        self.MIN_WORDS = 3
        self.THRESHOLD = 0.6
        self.MIN_DISTANCE = 0.000000001
        self.model = model
        self.unique_words = []
        # Common stopfilter
        self.filter = {'them', 'it', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
        self.host = sparqlmuse_host
        self.identifiers = []
        self.labels = {}
        self.embeddings = {} # Store embeddings for vector DB

    def clean_text(self, text):
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        text = re.sub(r'[^\\w\\s]', ' ', text)
        text = re.sub(r'\\s+', ' ', text)
        text = text.strip()
        
        words = text.split()
        seen = set()
        self.unique_words = []
        for word in words:
            word_lower = word.lower()
            if len(word_lower) >= self.MIN_WORDS or word[0].isupper():
                if word_lower not in seen:
                    seen.add(word_lower)
                    self.unique_words.append(word_lower) 

        final_words = []
        for w in self.unique_words:
            if w not in self.filter:
                final_words.append(w)
                
        return ' '.join(final_words)

    def get_wikipedia_candidates(self, term):
        """Query Wikipedia API to find candidate pages and their Wikidata IDs."""
        try:
            # 1. Search for candidates
            search_url = "https://en.wikipedia.org/w/api.php"
            search_params = {
                "action": "query",
                "list": "search",
                "srsearch": term,
                "format": "json"
            }
            headers = {
                "User-Agent": "HIPS-Alignment-Bot/1.0 (https://github.com/4tikhonov/rosetta-ai; vyacheslav.tykhonov@gmail.com)"
            }
            if self.DEBUG:
                print(f"[CosineDistance] Wikipedia Search for: {term}")
            
            search_response = requests.get(search_url, params=search_params, headers=headers, timeout=10)
            if search_response.status_code != 200:
                if self.DEBUG: print(f"Search API failed: {search_response.status_code}")
                return []
                
            search_data = search_response.json()
            search_results = search_data.get('query', {}).get('search', [])
            
            if not search_results:
                if self.DEBUG: print(f"[CosineDistance] No Wikipedia results for: {term}")
                return []
                
            # Take top 3 search results
            titles = [res['title'] for res in search_results[:3]]
            if self.DEBUG: print(f"Found titles: {titles}")
            
            # 2. Get Wikidata IDs for these titles
            props_params = {
                "action": "query",
                "prop": "pageprops|extracts",
                "ppprop": "wikibase_item",
                "exintro": 1,
                "explaintext": 1,
                "titles": "|".join(titles),
                "redirects": 1,
                "format": "json"
            }
            
            props_response = requests.get(search_url, params=props_params, headers=headers, timeout=10)
            if props_response.status_code != 200:
                if self.DEBUG: print(f"Props API failed: {props_response.status_code}")
                return []
                
            props_data = props_response.json()
            if self.DEBUG: print(f"Props Response Keys: {props_data.keys()}")
            pages = props_data.get('query', {}).get('pages', {})
            if self.DEBUG: print(f"Pages found: {len(pages)}")
            
            candidates = []
            for page_id, page_info in pages.items():
                if self.DEBUG: print(f"  Checking page: {page_id} - {page_info.get('title')}")
                if page_id == "-1": continue
                
                wikidata_id = page_info.get('pageprops', {}).get('wikibase_item')
                if wikidata_id:
                    if self.DEBUG: print(f"    -> match found: {page_info.get('title')} -> {wikidata_id}")
                    candidates.append({
                        "title": wikidata_id,
                        "label": page_info.get('title'),
                        "description": page_info.get('extract', '')[:200]
                    })
                else:
                    if self.DEBUG: print(f"    -> No wikidata_id for {page_info.get('title')}")
            
            return candidates
            
        except Exception as e:
            if self.DEBUG:
                print(f"[CosineDistance] Wikipedia fallback error: {e}")
            return []

    def get_candidates(self, term, context):
        try:
            wikilink = f"{self.host}/wikilink/?term={term}&context={context}&language=en&format=json"
            if self.DEBUG:
                print(f"[CosineDistance] Querying: {wikilink}")
            
            response = requests.get(wikilink, timeout=30)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict):
                    if 'title' in data:
                        return [data]
                    if 'candidates' in data:
                        return data['candidates']
            else:
                 if self.DEBUG:
                     print(f"[CosineDistance] API Error: {response.status_code}")
        except Exception as e:
            if self.DEBUG:
                print(f"[CosineDistance] Error querying SparqlMuse: {e}")
        return []

    def get_best_match(self, term, context):
        input_text = f"{term} {context}"
        self.full_embedding = self.model.encode([input_text])[0].tolist()
        
        # 1. Try SparqlMuse
        candidates = self.get_candidates(term, context)
        
        # 2. Fallback to Wikipedia if no SparqlMuse results
        if not candidates:
            if self.DEBUG:
                print(f"[CosineDistance] No SparqlMuse results, trying Wikipedia fallback for: {term}")
            candidates = self.get_wikipedia_candidates(term)
            
        if not candidates:
            return []
            
        candidate_texts = []
        valid_candidates = []
        
        for cand in candidates:
            c_label = cand.get('label', '')
            c_desc = cand.get('description', '')
            c_text = f"{c_label} {c_desc}"
            candidate_texts.append(c_text)
            valid_candidates.append(cand)
            
        if not candidate_texts:
            return []
            
        candidate_embeddings = self.model.encode(candidate_texts)
        input_emb_tensor = self.model.encode([input_text])
        distances = cosine_distances(input_emb_tensor, candidate_embeddings)[0]
        
        results = []
        for i, dist in enumerate(distances):
            sim = 1 - dist
            cand = valid_candidates[i]
            
            if self.DEBUG:
                print(f"  Candidate: {cand.get('label')} ({cand.get('title')}) - Similarity: {sim:.4f}")
                
            if dist < self.THRESHOLD:
                cand['score'] = float(sim)
                results.append(cand)
                
                q_id = cand.get('title')
                if q_id:
                    self.identifiers.append(q_id)
                    self.labels[q_id] = cand.get('label', '')

        results.sort(key=lambda x: x['score'], reverse=True)
        return [r.get('title') for r in results if r.get('title')]

def main():
    parser = argparse.ArgumentParser(description="align HIPS hazards to Wikidata.")
    parser.add_argument("--input", default="data/final_translations.csv", help="Input CSV file")
    parser.add_argument("--output", default="output/alignment_wikidata.json", help="Output JSON file")
    parser.add_argument("--sparqlmuse", default="https://sparqlmuse.now.museum", help="SparqlMuse API")
    parser.add_argument("--debug", action="store_true", help="Enable debug")
    parser.add_argument("--model", default="all-MiniLM-L6-v2", help="Sentence transformer model")
    
    # Vector DB Args
    parser.add_argument("--vector-store", default="chroma", choices=["chroma", "qdrant", "file"], help="Vector Store Type")
    parser.add_argument("--collection", default="hips_alignment", help="Collection Name")
    parser.add_argument("--qdrant-host", default="localhost", help="Qdrant Host")
    parser.add_argument("--qdrant-port", type=int, default=6333, help="Qdrant Port")
    parser.add_argument("--term", help="Single term to align (overrides input file)")
    parser.add_argument("--context", default="", help="Context description for the single term")
    parser.add_argument("--retry-empty", action="store_true", help="Retry alignment for terms that have empty results in the output file")
    
    args = parser.parse_args()

    # Load Model ONCE
    print(f"Loading model: {args.model}...")
    device = "cpu"
    if torch.cuda.is_available(): device = "cuda"
    elif torch.backends.mps.is_available(): device = "mps"
    model = SentenceTransformer(args.model, device=device)
    print(f"Model loaded on {device}.")

    # Init Vector Store
    v_store = VectorStore(
        store_type=args.vector_store, 
        collection_name=args.collection,
        qdrant_host=args.qdrant_host,
        qdrant_port=args.qdrant_port
    )

    if args.term:
        print(f"Processing single term: {args.term}")
        df = pd.DataFrame([{'term': args.term, 'context': args.context}])
    else:
        if not os.path.exists(args.input):
            print(f"Input file not found: {args.input}")
            return
        df = pd.read_csv(args.input)
        
        # CLEAN and Deduplicate
        if 'term' in df.columns:
            df['term'] = df['term'].astype(str).str.strip()
        if 'context' in df.columns:
            df['context'] = df['context'].astype(str).str.strip()
            
        subset = ['term']
        if 'context' in df.columns:
            subset.append('context')
            
        initial_len = len(df)
        df.drop_duplicates(subset=subset, inplace=True)
        print(f"Processing {len(df)} unique terms (dropped {initial_len - len(df)} duplicates) from {args.input}...")
    
    # Load existing results if they exist to support resuming
    results = {}
    if os.path.exists(args.output):
        try:
            with open(args.output, 'r') as f:
                results = json.load(f)
            print(f"Loaded {len(results)} existing alignments from {args.output}")
        except Exception as e:
            print(f"Warning: Could not load existing output file: {e}")

    for index, row in df.iterrows():
        term = row.get('term')
        context_text = row.get('context', '')
        if not term or term == "nan": continue
        
        # Skip if already processed in this run or previous run
        # Unless it's empty and we are retrying
        if term in results:
            # If we have results, skip
            # If we DON'T have results (empty list), skip only if NOT retrying
            if results[term] or not args.retry_empty:
                if args.debug:
                    print(f"Skipping already aligned term: {term}")
                continue
            else:
                if args.debug:
                    print(f"Retrying empty alignment for: {term}")

        query_text = f"{term} {context_text}"
        
        if args.debug:
            print(f"\nAnalyzing [{index}]: {term}")

        try:
            aligner = CosineDistance(query_text, model, debug=args.debug, sparqlmuse_host=args.sparqlmuse)
            ids = aligner.get_best_match(term, context_text)
            
            meta = {
                "term": term, 
                "context_prefix": context_text[:100],
                "wikidata_ids": json.dumps(ids)
            }
            
            v_store.add(id=term, text=query_text, embedding=aligner.full_embedding, metadata=meta)

            if ids:
                results[term] = []
                print(f"[{term}] -> {ids}")
                for qid in ids:
                    results[term].append({
                        "id": qid,
                        "label": aligner.labels.get(qid, ""),
                        "uri": f"https://www.wikidata.org/wiki/{qid}"
                    })
            else:
                # Still record that we tried but found no match to avoid re-processing
                results[term] = []
                if args.debug: print(f"[{term}] -> No match found.")
            
            # Incremental save after each concept
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
                    
        except Exception as e:
            print(f"Error processing {term}: {e}")
            if args.debug:
                import traceback
                traceback.print_exc()
    
    print(f"\nAlignment complete. Final mappings in {args.output}")

if __name__ == "__main__":
    main()
