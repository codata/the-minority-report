
import spacy
import sys
import os

def test_model(model_path):
    print(f"Loading model from: {model_path}")
    try:
        nlp = spacy.load(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    test_texts = [
        "A thunderstorm is a meteorological phenomenon.",
        "The term drought in French is sécheresse.",
        "Flooding can cause significant damage to infrastructure.",
        "Avalanche risk is high in the mountains.",
        "Peste des petits ruminants is a viral disease.",
        "Translate 'Heat wave' into Spanish.",
        "В Испании произошла вторая железнодорожная авария за три дня", # Russian: Train accident
        "falen van kritieke infrastructuur in nederland", # Dutch: Critical infrastructure failure
        "Con il termine cyberbullismo si intende qualunque forma di pressione", # Italian: Cyberbullying
    ]

    print("\n=== Testing Model Performance ===")
    for text in test_texts:
        doc = nlp(text)
        print(f"\nText: {text}")
        if not doc.ents:
             print("  [No entities found]")
        for ent in doc.ents:
            print(f"  - '{ent.text}' ({ent.label_})")

if __name__ == "__main__":
    # Default path or argument
    path = "training/spacy_model"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    
    # If path is a directory with run_X subdirectories, use run_0
    if os.path.isdir(path):
        run_0_path = os.path.join(path, "run_0")
        if os.path.exists(run_0_path):
            print(f"Found parallel training output. Using model from: {run_0_path}")
            path = run_0_path
    
    if not os.path.exists(path):
        print(f"Model path not found: {path}")
        print("Please train the model first using: python3 training/train-spacy.py")
    else:
        test_model(path)
