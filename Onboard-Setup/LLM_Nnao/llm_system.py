from transformers import AutoModelForCausalLM
from memory_lane import load_memory
from emotion_core import get_current_emotion

conversation_memory = []

# Load the base model
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Add multiple adapters for different tasks
model.add_adapter("emotion_adapter", config="emotion_adapter_config.json")
model.add_adapter("memory_adapter", config="memory_adapter_config.json")

# Activate both emotion and memory adapters
model.set_active_adapters(["emotion_adapter", "memory_adapter"])


def build_prompt(user_input, sys_prompt='', enable_emotions=True):
    if sys_prompt == '':
        sys_prompt = "You are Nova, a curious young AI who is still learning about the world around you and ask questions when confused."
    memory = load_memory()
    emotion = get_current_emotion()
    prompt = f"<|system prompt|>\n{sys_prompt}\n<|memories<|>\n{memories}\n"
    if enable_emotions:
        prompt += f"<|current emotion|>\n{emotion}\n"
    prompt += f"<|user|>\n{user_input}\n<|nova|>"
    return prompt

def get_response(input_text, prompt=''):
    if prompt == '':
        prompt = build_prompt(input_text)
    inputs = tokenizer(input_text, return_tensors="pt")
    output = model.generate(**inputs)

    # Decode and print the output
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    print(decoded_output)