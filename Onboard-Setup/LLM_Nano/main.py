from llm_system import get_response
from sensors import listen, speak
import re
from time import sleep
from memory_lane import remember, forget
import rest

def main_loop():
    while True:
        user_input = listen()
        match = re.search('sleep', user_input.lower())
        if match:
            rest.sleep_cycle()
        response = get_response(user_input)
        speak(respomse)
        sleep(0.1)