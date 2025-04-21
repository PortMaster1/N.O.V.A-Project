import asyncio
from server import send_states, get_response
from sensors import get_states

async def send_state_loop():
    while True:
        await send_states()

def main_loop():
    while True:
        asyncio.run()