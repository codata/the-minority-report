# Training Guide

This guide covers training custom models on the multilingual disaster risk terminology dataset.

## Overview

The Minority Report supports two training approaches:

1. **spaCy NER** - Lightweight, fast, production-ready (Recommended)
2. **Transformers** - Advanced fine-tuning for translation tasks

## spaCy NER Training (Recommended)

### What It Does

Trains a Named Entity Recognition model to identify:
- **DISASTER_TERM** - Disaster risk terminology in English
- **TRANSLATION** - Translated terms in target languages

### Quick Start

```bash
# Install dependencies
pip install spacy

# Train the model
python3 training/train-spacy.py --data-dir output --n-iter 30 --test

# Output: training/spacy_model/
```

### Usage

```python
import spacy

# Load trained model
nlp = spacy.load("training/spacy_model")

# Extract entities
doc = nlp("A thunderstorm is a meteorological phenomenon.")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")
```

### Parameters

- `--data-dir` - Directory containing Croissant JSON files (default: `output`)
- `--output-dir` - Where to save the model (default: `training/spacy_model`)
- `--n-iter` - Number of training iterations (default: 30)
- `--test` - Run test examples after training

### Performance

- **Training time:** 1-2 minutes
- **Model size:** ~10MB
- **Hardware:** CPU or GPU
- **Accuracy:** High for terminology extraction

## Transformers Fine-tuning (Advanced)

### What It Does

Fine-tunes a Gemma language model for multilingual translation with context awareness.

### Requirements

- NVIDIA GPU with CUDA
- 16GB+ VRAM
- Linux environment

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python3 training/train.py \
  --data-dir output \
  --model-name google/gemma-2-2b-it \
  --max-steps 60
```

### Parameters

- `--data-dir` - Directory containing Croissant JSON files
- `--model-name` - HuggingFace model ID (default: `google/gemma-2-2b-it`)
- `--output-dir` - Where to save the model (default: `training/fine_tuned_model`)
- `--max-steps` - Number of training steps (default: 60)

### Performance

- **Training time:** 15-30 minutes (GPU-dependent)
- **Model size:** ~2GB (LoRA adapters)
- **Hardware:** CUDA GPU required
- **Accuracy:** High for context-aware translation

## Data Format

Both training scripts automatically load data from Croissant JSON-LD files:

```json
{
  "name": "Thunderstorm",
  "description": "A thunderstorm is defined as...",
  "https://schema.org/identifier": "MH0103",
  "sc:alternateName": [
    {"@value": "orage", "@language": "fr"},
    {"@value": "tormenta", "@language": "es"}
  ]
}
```

## Troubleshooting

### spaCy Training Issues

**Error: Overlapping entities**
- Fixed in latest version
- Entities are now in separate training examples

**Error: List object has no attribute 'lower'**
- Fixed in latest version
- Handles both string and list formats for multilingual names

### Transformers Training Issues

**Error: CUDA out of memory**
- Reduce `per_device_train_batch_size` to 1
- Use a smaller model (e.g., `google/gemma-2-1b`)

**Error: Training stuck at 0%**
- First step can take 1-3 minutes
- Wait for CUDA kernel compilation
- Check GPU utilization with `nvidia-smi`

## Next Steps

After training:

1. **Test the model** on new terminology
2. **Deploy to production** (spaCy models are lightweight)
3. **Integrate with MCP server** for LLM-assisted workflows
4. **Export to GGUF** (Transformers only) for Ollama integration

## References

- [spaCy Training Documentation](https://spacy.io/usage/training)
- [Transformers Fine-tuning Guide](https://huggingface.co/docs/transformers/training)
- [PEFT LoRA Documentation](https://huggingface.co/docs/peft/conceptual_guides/lora)
