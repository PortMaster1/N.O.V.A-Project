import asyncio, requests, os, serial, pyttsx3
from time import sleep
from sensors import listen, speak
from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_env
import RPi.GPIO as GPIO

# Testimg Imports Here:
import threading, os
from dotenv import load_env
# Class Imports
from server import Client
from signals import Signals

# End Testing Importa

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

"""
try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Turn LED on
        time.sleep(1)
        GPIO.output(17, GPIO.LOW)   # Turn LED off
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
"""

load_dotenv(overwrite=True)

# Initialize STT and TTS Engines
model = WhisperModel("base.en", compute_type="int8")  # Use "tiny", "base", or "small" for speed
#tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
engine = pyttsx3.init()

"""
async def send_state_loop():
    while True:
        x, y, z, tilt = await read_microbit()
        await send_states(x, y, z, tilt)
        await asyncio.sleep(0.1)
"""

# The main class that runs the whole client.
class Main:
    def __init__(self):
        while True:
            text = self.listen()
            reaponse = self.get_response(text)
            self.speak(response)
            sleep(0.1)
    
    def send_states(self, x, y, z, tilt):
        requests.post(STATE_URL, json={"states": [x, y, z, tilt]})
        return
    
    def get_response(self, text, model="day_model"):
        # REST API URL of your LLM server
        IP = "192.168.12.138:8000"            # Update IP Address
        CHAT_URL = f"http://{IP}/api/chat"
        STATE_URL = f"http://{IP}/api/state"
        response = requests.post(CHAT_URL, json={"message": text})
        return response.json()["response"]
    
    # Listen Functiom
    def listen(self):
        fs = 16000  # Whisper likes 16kHz mono
        seconds = 5
        print("Listening...")
        # TODO: Add LED to show listening
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sleep(5)
        sd.wait()
        print("Finished Listening.")
        # TODO: Add LED to show finished listening and procceasing
        write("audio.wav", fs, recording)
        print("Finished writing")
        segments, info = model.transcribe("audio.wav", beam_size=5)
        result = "".join([segment.text for segment in segments])
        print(f"[USER] {result}")
        return result
    
    # Speak the response from the LLM
    def speak(self, response_text, filename="response.wav"):
        # TODO Add LED for finished processing
        print(f"[NOVA] {response_text}")
        #tts_model.tts_to_file(text=response_text, file_path=filename)
        engine.say(response_text)
        engine.runAndWait()
        #os.system(f"aplay {filename}" if os.name != 'nt' else f"start {filename}")

async def llm_loop():
    while True:
        text = listen()
        response = await get_response(text)
        speak(response)
        await asyncio.sleep(0.1)

def main_loop():
    #asyncio.run(send_state_loop)
    #asyncio.run(llm_loop)
    m = Main()

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Operation Terminated")

# Testing Starts Here:
load_env(overwrite = True)

HOST = os.getenv("SOCKET_HOST")
PORT = os.getenv("SOCKET_PORT")



def main_loop(HOST, PORT):
    signals = Signals()
    client = Client(HOST, PORT, signals)
    
    

if __name__ == "__main__":
    main_loop(HOST, PORT)