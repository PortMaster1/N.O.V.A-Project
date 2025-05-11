import memory_lane
from mem0 import Memory
import emotion_core
from ollama import chat, ChatResponse
import asyncio
import time

# Stopwatch
start = None

# Persistsnt mem0 Memory
config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "llama3.1:1B"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    },
}

memory = Memory.from_config(config)

# Temporary Conversation Memory
chat_mem = []

# Functions callable by LLM
available_functions = {}

async def get_response(message: str, model: str = "nova4.1", user_id: str = "default_user") -> str:
    global chat_mem
    global start
    if not start:
        start = time.perf_counter()
    end = time.perf_counter()
    if end - start > 60:
        if not chat_mem == []:
            memory.add(chat_mem, user_id=user_id)
            chat_mem = []
    
    relevant_memories = memory.search(query=message, user_id=user_id)
    if relevant_memories:
        prompt = f"User input: {question}\nPrevious memories: {'\n'.join(previous_memories)}"
    else:
        prompt = f"User input: {question}"
    
    memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
    chat_mem.append({"role": "user", "content": message},)
    #response = chat(model, messages=chat_mem, tools=[update_memory, update_emotions, remember, forget]
    response = chat(model, messages=chat_mem)
    print(response.message.content)
    chat_mem.append ({"role": "assistant", "content": response message content} ,)
    
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
    start = time.perf_counter()
    return response.message.content


if __name__ == '__main__':
    try:
        while True:
            message = input(" You say:")
            #asyncio.run(get_response(input_text))
            get_response(message)
    except KeyboardInterrupt:
        print("Goodbye!")
