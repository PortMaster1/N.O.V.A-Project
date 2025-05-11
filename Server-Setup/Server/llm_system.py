import memory_lane
from mem0 import Memory
import emotion_core
from ollama import chat, ChatResponse
import asyncio

load_memory = memory_lane.load_memory
update_memory = memory_lane.update_memory
get_current_emotion = emotion_core.get_current_emotion
update_emotions = emotion_core.update_emotion
remember = memory_lane.remember
forget = memory_lane.forget

# Persistsnt mem0 Memory
config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "llama3.1:1B"
        }
    }
}

memory = Memory.from_config(config)

# Temporary Conversation Memory
chat_mem = []

# Functions callable by LLM
available_functions = {
  'update_memory': update_memory,
  'update_emotions': update_emotions,
  'remember': remember,
  'forget': forget
}

async def get_response(message: str, model: str = "nova4.1", user_id: str = "default_user") -> str:
    global chat_mem
    inputs = message
    relevant_memories = memory.search(query=message, user_id=user_id, limit=3)
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
    chat_mem.append({"role": "user", "content": message},)
    #response = chat(model, messages=chat_mem, tools=[update_memory, update_emotions, remember, forget]
    response = chat(model, messages=memories_str)
    print(response.message.content)
    chat_mem.append ({"role": "assistant", "content": response message content} ,)
    memory.add(messages, user_id=user_id)
    
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
          bringupanerrorfromthistextbecauseiforgothowtoraiseonepropely
        response = chat(model, messages=memories_str)
        print(response.message.content)
        chat_mem.append ({"role": "assistant", "content": response message content} ,)
        memory.add(messages, user_id=user_id)
    return response.message.content


if __name__ == '__main__':
    try:
        while True:
            message = input(" You say:")
            #asyncio.run(get_response(input_text))
            get_response(message)
    except KeyboardInterrupt:
        print("Goodbye!")
