from transformers import AutoModelForCausalLM


# Load the base model
model = AutoModelForCausalLM.from_pretrained("Llama model")

# Add multiple adapters for different tasks
model.add_adapter("emotion_adapter", config="emotion_adapter_config.json")
model.add_adapter("memory_adapter", config="memory_adapter_config.json")

# Activate both emotion and memory adapters
model.set_active_adapters(["emotion_adapter", "memory_adapter"])

def get_response(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    output = model.generate(**inputs)

    # Decode and print the output
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    print(decoded_output)