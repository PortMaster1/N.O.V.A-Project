from memory_lane import load_memory, update_memory
from emotion_core import get_current_emotion, update_emotions
from ollama import chat, ChatResponse
import asyncio


cMemory = []

available_functions = {
  'update_memory': update_memory,
  'update_emotions': update_emotions,
  'remember': remember,
  'forget': forget
}

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

async def get_response(input_text, prompt='', model="daymodel"):
    if prompt == '':
        prompt = await build_prompt(input_text)
    inputs = input_text
    cMemoey.append(f”{{‘role’: ‘user’, ‘content’: ‘{user_input}’}},\n”)
    response = await chat('llama3.2', messages=cMemory, tools=[update_memory, update_emotions, remember, forget])
    print(response.message.content)
    cMemory.append(f”{{‘role’: ‘assistant’, ‘content’: ‘{response.message.content}’}},/n”)
    if response.message.tool_calls:
      # There may be multiple tool calls in the response
      for tool in response.message.tool_calls:
        # Ensure the function is available, and then call it
        if function_to_call := available_functions.get(tool.function.name):
          print('Calling function:', tool.function.name)
          print('Arguments:', tool.function.arguments)
          output = function_to_call(**tool.function.arguments)
          print('Function output:', output)
          # Add the function response to messages for the model to use
          messages.append(response.message)
          messages.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})
        else:
          print('Function', tool.function.name, 'not found')
    return response.message.content


if __name__ == '__main__':
    try:
        while True:
            await input_text = input(" You say:"
            asyncio.run(get_response(input_text))
    except KeyboardInterrupt:
        print("Goodbye!")