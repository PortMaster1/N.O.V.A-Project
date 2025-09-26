import asyncio, requests, re
import asyncio
import json
import discord

intents = discord.Intents.default()
intents.message_content = True

class Discord_Client:
	def __init__(self, signals):
		self.signals = signals
	
	# Runs the client alltogether
	async def run(self):
		bot = discord.Bot()
		connections = {}
		
		@bot.event
		async def on_ready():
			print("DISCORD BOT IS READY")
			pm1 = await bot.fetch_user("USER_ID")
			await pm1.send("Online")
			self.channel = await pm1.create_dm()
		
		@bot.event
		async def on_message(message):
			if message.author == bot.user:
				return
			if message.channel not in connections:
				connections.append(message.channel)
			# Add the message to the history and mark a new message.
			self.signals.history.append({"role":"user", "content":message.content})
			self.signals.new_message = True
		
		@bot.slash_command(name="ping", description="Check the bot's status")
		async def ping(ctx):
			await ctx.respond(f"Pong! {bot.latency}")
		
		# Starts the "is typing..." text on Discord
		async def start_typing():
			while not self.signals.terminate:
				if self.signals.AI_thinking:
					await self.channel.typing()
					await asyncio.sleep(10)
		
		async def message_waiter():
			if self.signals.history = []:
				message = ""
			else:
				message = self.signals.history[-1]
			while not self.signals.terminate:
				if self.signals.history[-1] != message:
					message = self.signals.history[-1]
					if not self.signals.AI_speaking:
						await send_initial(message["content"])
					else:
						await send_message(message["content"])
		
		# Send the initial message for the response
		async def send_initial(message):
			self.signals.AI_speaking = True
			self.message = await self.channel.send(message)
		
		# Edit the previously created message to include the additional chunk
		async def send_message(message):
			await self.message.edit(message)
		
		# Create the start_typing task, the message_waiter task, and start the bot
		asyncio.create_task(message_waiter())
		asyncio.create_task(start_typing())
		bot.run("TOKEN", status="online")


if __name__ == "__main__":
	from signals import Signals
	import threading
	signals = Signals()
	client = Discord_Client(signals)
	client_thread = threading.Thread(target=client.run, dameon=True)
	client_thread.start()