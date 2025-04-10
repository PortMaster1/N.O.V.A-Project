from transformers import AdapterTrainer, AutoModelForCausalLM
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, TaskType

dataset = load_dataset("json", data_files="emotion_data.jsonl", split="train")

def format_prompt(example):
    return {
        "text": f"### Instruction:\n{example['instruction']}\n\n### Input:\n{example['input']}\n\n### Response:\n{example['output']}"
    }

dataset = dataset.map(format_prompt)

from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, load_in_8bit=True, device_map="auto")

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],  # or use layer names relevant to your model
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

model = get_peft_model(model, lora_config)

# Define a training loop for the adapter
trainer = AdapterTrainer(
    model=model,
    train_dataset=train_data,
    eval_dataset=eval_data,
    args=training_args
)

# Start training
trainer.train()