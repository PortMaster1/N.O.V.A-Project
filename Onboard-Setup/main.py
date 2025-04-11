from llm_system import get_response
from sensors import listen, speak
import re
from memory_lane import remember, forget
import rest

def main_loop():
    user_input = listen()
    match = re.search('sleep nova', user_input.lower())
    if match:
        rest.rest()
    response = get_response(user_input)
    match = re.search(r'\[ACTION: (.*?)\]', response)
    if match:
        text = match.group(1).split()
        action = text[0]
        args = text[1:]
        if action == "turn_head":
            turn_head(*args)
        response.replace(r'\[ACTION: (.*?)\]', '')
    match = re.search(r'\[REMEMBER: (.*?)\]', response)
    if match:
        text = match.group(1).split()
        menory = text[0:]
        remember(memory)
        response.replace(r'\[REMEMBER: (.*?)\]', '')
    match = re.search(r'\[FORGET: (.*?)\]', response)
    if match:
        text = match.group(1).split()
        memory = text[0:]
        forget(memory)
        response.replace(r'\[FORGET: (.*?)\]', '')
    speak(respomse)