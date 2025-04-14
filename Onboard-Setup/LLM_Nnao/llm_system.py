from memory_lane import load_memory
from emotion_core import get_current_emotion
from ollama import AsyncClient
import asyncio


cMemory = []

# TODO: FINISH
# Add multiple adapters for different tasks
model.add_adapter("emotion_adapter", config="emotion_adapter_config.json")
model.add_adapter("memory_adapter", config="memory_adapter_config.json")

# TODO: FINISH
# Activate both emotion and memory adapters
model.set_active_adapters(["emotion_adapter", "memory_adapter"])


async def build_prompt(user_input, sys_prompt='', enable_emotions=True):
    if sys_prompt == '':
        sys_prompt = "You are Nova, a curious young AI who is still learning about the world around you and ask questions when confused."
    memory = load_memory()
    emotion = get_current_emotion()
    prompt = f"<|system prompt|>\n{sys_prompt}\n<|memories<|>\n{memories}\n"
    if enable_emotions:
        prompt += f"<|current emotion|>\n{emotion}\n"
    prompt += f"<|user|>\n{user_input}\n<|nova|>"
    return prompt

async def get_response(input_text, prompt=''):
    client = AsyncClient()
    if prompt == '':
        prompt = await build_prompt(input_text)
    inputs = input_text
    cMemoey.append(f”{{‘role’: ‘user’, ‘content’: ‘{user_input}’}},\n”)
    output = await client.char('llama3.2', messages=cMemory)
    print(output.message.content)
    cMemory.append(f”{{‘role’: ‘assistant’, ‘content’: ‘{output.message.content}’}},/n”)
    return output.message.content


if __name__ == '__main__':
    try:
        while True:
            await input_text = input(" You say:"
            asyncio.run(get_response(input_text))