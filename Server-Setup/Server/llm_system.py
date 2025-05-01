import memory_lane
import emotion_core
from ollama import chat, ChatResponse
import asyncio

load_memory = memory_lane.load_memory
update_memory = memory_lane.update_memory
get_current_emotion = emotion_core.get_current_emotion
update_emotions = emotion_core.update_emotion
remember = memory_lane.remember
forget = memory_lane.forget

chat_mem = []

available_functions = {
  'update_memory': update_memory,
  'update_emotions': update_emotions,
  'remember': remember,
  'forget': forget
}

async def get_response(input_text, model="day_model"):
    global chat_mem
    inputs = input_text
    chat_mem.append({"role": "user", "content": input_text},)
    #response = chat(model, messages=chat_mem, tools=[update_memory, update_emotions, remember, forget]
    response = chat(model, messages=chat_mem)
    print(response.message.content)
    chat_mem.append({"role": "assistant", "content": response.message.content},)
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
          chat_mem.append(response.message)
          chat_mem.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})
        else:
          print('Function', tool.function.name, 'not found')
    return response.message.content


if __name__ == '__main__':
    try:
        while True:
            input_text = input(" You say:")
            asyncio.run(get_response(input_text))
    except KeyboardInterrupt:
        print("Goodbye!")
