import asyncio
from server import send_states, get_response
from sensors import read_microbit, listen, speak

async def send_state_loop():
    while True:
        x, y, z, tilt = read_microbit()
        await send_states(x, y, z, tilt)

def main_loop():
    while True:
        asyncio.run()