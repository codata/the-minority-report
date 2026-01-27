
import json

def load_index():
    with open('data/index_cache.json', 'r') as f:
        data = json.load(f)
        print(f"Loaded {len(data)} items from index")
        return data

if __name__ == "__main__":
    load_index()
