from transformers import AdapterTrainer, AutoModelForCausalLM

from datasets import load_dataset

dataset = load_dataset("json", data_files="emotion_data.jsonl", split="train")

def format_prompt(example):
    return {
        "text": f"### Instruction:\n{example['instruction']}\n\n### Input:\n{example['input']}\n\n### Response:\n{example['output']}"
    }

dataset = dataset.map(format_prompt)

# Define a training loop for the adapter
trainer = AdapterTrainer(
    model=model,
    train_dataset=train_data,
    eval_dataset=eval_data,
    args=training_args
)

# Start training
trainer.train()