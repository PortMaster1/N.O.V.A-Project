# Python Imports
import asyncio
import time
import configparser

# Local Imports
from ollama import ChatResponse, AsyncClient

# for the LLM model
config = configparser.ConfigParser()
config.read('config.ini')
config = config['DEFAULT']

class LLM_System:
	def __init__(self, signals):
		self.signals = signals
		# Functions callable by LLM
		self.aval_functions = {}
		
	async def get_response(self, model: str = None, user_id: str = "default_user"):
		if not model:
			model = config["model"]
		# TODO: Do this: v
		#response = chat(model, messages=chat_mem, tools=[update_memory, update_emotions, remember, forget]
		async for chunk in await AsyncClient().chat(model=model,messages=self.signals.history, streaming=True):
			if not self.signals.AI_speaking:
				self.signals.history[{"role":"assistant","content":chunk['message']['content']}]
			else:
				self.signals.history[-1]["content"] += chunk['message']['content']
		
	def run(self):
		print("LLM IS RUNNING")
		while not self.signals.terminate:
			if self.signals.new_message:
				self.signals.new_message = False
				await self.get_response()


# TODO: Implement tool stuff v
"""
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
		chat_mem.append ({"role": "assistant", "content": response.message.content})
"""
	
if __name__ == '__main__':
	from signals import Signals
	import threading
	signals = Signals()
	llm = LLM_System(signals)
	llm_thread = threading.Thread(target=llm.run, dameon=True)
	try:
		while True:
			message = input(" You say:")
			message = {"role":"user","content":message}
			signals.history.append(message)
			if self.signals.history[-1] != message:
				print(self.signals.history[-1]["content"])
	except KeyboardInterrupt:
		print("Goodbye!")