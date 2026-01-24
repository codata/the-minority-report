
import json
import glob
import os
import argparse
import torch
from datasets import Dataset
from unsloth import FastLanguageModel
from trl import SFTTrainer
from transformers import TrainingArguments

def load_croissant_data(data_dir):
    """
    Loads all Croissant JSON-LD files from the directory and converts them 
    into an instruction tuning dataset.
    """
    training_samples = []
    files = glob.glob(os.path.join(data_dir, "croissant_*.json"))
    
    print(f"Found {len(files)} Croissant files in {data_dir}")
    
    for file_path in files:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                
            # Extract Core Metadata
            term = data.get("name", "Unknown Term")
            context = data.get("description", "")
            
            # Extract HIPS Identifier (if available)
            identifier = data.get("https://schema.org/identifier", "")
            
            # Extract Translations from alternateName
            # Format: [{"@value": "...", "@language": "...", "creator": ...}]
            alternates = data.get("sc:alternateName", [])
            
            if not alternates:
                continue
                
            for alt in alternates:
                lang = alt.get("@language")
                translation = alt.get("@value")
                
                if not lang or not translation:
                    continue
                    
                # Skip English to English if it's just the term itself, 
                # unless we want to train it to define? 
                # Let's focus on translation instructions.
                if lang == "en" and translation.lower() == term.lower():
                    continue
                
                # Construct Output
                # If HIPS code exists, we want the model to output it.
                output_text = translation
                if identifier:
                    output_text += f" (HIPS: {identifier})"
                
                # Construct Instruction
                instruction = f"Translate the term '{term}' into {lang} based on the provided disaster risk context."
                if identifier:
                    instruction += " Include the HIPS reference code."
                    
                training_samples.append({
                    "instruction": instruction,
                    "input": context,
                    "output": output_text
                })
                
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    return training_samples

def train(args):
    # 1. Configuration
    max_seq_length = 2048 # Choose any! We auto support RoPE Scaling internally!
    dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
    load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

    # 2. Load Model
    print(f"Loading model: {args.model_name}")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = args.model_name,
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )

    # 3. Add LoRA Adapters
    model = FastLanguageModel.get_peft_model(
        model,
        r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
        target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                          "gate_proj", "up_proj", "down_proj",],
        lora_alpha = 16,
        lora_dropout = 0, # Supports any, but = 0 is optimized
        bias = "none",    # Supports any, but = "none" is optimized
        use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
        random_state = 3407,
        use_rslora = False,  # We support rank stabilized LoRA
        loftq_config = None, # And LoftQ
    )

    # 4. Prepare Data
    print("Loading data...")
    raw_data = load_croissant_data(args.data_dir)
    print(f"Loaded {len(raw_data)} training examples.")
    
    if len(raw_data) == 0:
        print("No training data found. Exiting.")
        return

    dataset = Dataset.from_list(raw_data)

    # Alpaca Prompt Format
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

    EOS_TOKEN = tokenizer.eos_token # Must add EOS_TOKEN
    
    def formatting_prompts_func(examples):
        instructions = examples["instruction"]
        inputs       = examples["input"]
        outputs      = examples["output"]
        texts = []
        for instruction, input, output in zip(instructions, inputs, outputs):
            text = alpaca_prompt.format(instruction, input, output) + EOS_TOKEN
            texts.append(text)
        return { "text" : texts, }

    dataset = dataset.map(formatting_prompts_func, batched = True)

    # 5. Training
    print("Starting training...")
    trainer = SFTTrainer(
        model = model,
        tokenizer = tokenizer,
        train_dataset = dataset,
        dataset_text_field = "text",
        max_seq_length = max_seq_length,
        dataset_num_proc = 2,
        packing = False, # Can make training 5x faster for short sequences.
        args = TrainingArguments(
            per_device_train_batch_size = 2,
            gradient_accumulation_steps = 1,
            warmup_steps = 5,
            max_steps = args.max_steps, # 60 steps is usually enough for small data
            learning_rate = 2e-4,
            fp16 = False,
            bf16 = False,
            logging_steps = 10,
            report_to = "none",
            optim = "adamw_8bit",
            weight_decay = 0.01,
            lr_scheduler_type = "linear",
            seed = 3407,
            output_dir = args.output_dir,
        ),
    )

    trainer.train()
    
    # 6. Save
    print(f"Saving model to {args.output_dir}...")
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    
    # 7. GGUF Export (Optional but requested for 'production ready' usage with Ollama)
    if args.export_gguf:
        print("Exporting to GGUF...")
        try:
            model.save_pretrained_gguf(args.output_dir, tokenizer, quantization_method = "q4_k_m")
            print(f"GGUF saved to {args.output_dir}")
        except Exception as e:
            print(f"GGUF Export failed (might need llama.cpp): {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fine-tune Gemma for Minority Report Translation")
    parser.add_argument("--data-dir", default="output", help="Directory containing Croissant JSON files")
    parser.add_argument("--model-name", default="unsloth/gemma-2-2b-it", help="Base model (HuggingFace/Unsloth ID)") 
    # Note: User asked for 'gemma3:1b'. If that exists on HF, put it here. 
    # Defaulting to a real Unsloth model for safety. User can override.
    parser.add_argument("--output-dir", default="training/fine_tuned_model", help="Output directory")
    parser.add_argument("--max-steps", type=int, default=60, help="Max training steps")
    parser.add_argument("--export-gguf", action="store_true", help="Export to GGUF format after training")
    
    args = parser.parse_args()
    
    train(args)
