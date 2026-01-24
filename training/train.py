
import json
import glob
import os
import argparse
import torch
from datasets import Dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

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
            alternates = data.get("sc:alternateName", [])
            
            if not alternates:
                continue
                
            for alt in alternates:
                lang = alt.get("@language")
                translation = alt.get("@value")
                
                if not lang or not translation:
                    continue
                    
                # Skip English to English if it's just the term itself
                if lang == "en" and translation.lower() == term.lower():
                    continue
                
                # Construct Output
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
    # 1. Load Model and Tokenizer
    print(f"Loading model: {args.model_name}")
    
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        load_in_4bit=True,
        device_map={"": torch.cuda.current_device()},
        torch_dtype=torch.float16,
    )
    
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # 2. Prepare model for training
    model = prepare_model_for_kbit_training(model)
    
    # 3. Configure LoRA
    lora_config = LoraConfig(
        r=16,
        lora_alpha=16,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # 4. Prepare Data
    print("Loading data...")
    raw_data = load_croissant_data(args.data_dir)
    print(f"Loaded {len(raw_data)} training examples.")
    
    if len(raw_data) == 0:
        print("No training data found. Exiting.")
        return

    # Alpaca Prompt Format
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

    EOS_TOKEN = tokenizer.eos_token
    
    # Tokenize the dataset
    def tokenize_function(examples):
        texts = []
        for instruction, input_text, output in zip(examples["instruction"], examples["input"], examples["output"]):
            text = alpaca_prompt.format(instruction, input_text, output) + EOS_TOKEN
            texts.append(text)
        
        return tokenizer(texts, truncation=True, max_length=2048, padding=False)

    dataset = Dataset.from_list(raw_data)
    tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)

    # 5. Training
    print("Starting training...")
    
    model.config.use_cache = False
    
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        max_steps=args.max_steps,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=10,
        report_to="none",
        optim="paged_adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        save_strategy="steps",
        save_steps=30,
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )

    trainer.train()
    
    # 6. Save
    print(f"Saving model to {args.output_dir}...")
    model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    
    print("Training complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fine-tune Gemma for Minority Report Translation")
    parser.add_argument("--data-dir", default="output", help="Directory containing Croissant JSON files")
    parser.add_argument("--model-name", default="google/gemma-2-2b-it", help="Base model (HuggingFace ID)")
    parser.add_argument("--output-dir", default="training/fine_tuned_model", help="Output directory")
    parser.add_argument("--max-steps", type=int, default=60, help="Max training steps")
    
    args = parser.parse_args()
    
    train(args)
