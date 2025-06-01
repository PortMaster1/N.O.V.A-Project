import os, serial
from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import asyncio
import requests
from time import sleep

# Initialize STT and TTS Engines
model = WhisperModel("tiny", compute_type="int8")  # Use "tiny", "base", or "small" for speed
#tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
engine = pyttsx3.init()

# Listen function
def listen():
    fs = 16000  # Whisper likes 16kHz mono
    seconds = 5
    print("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sleep(5)
    sd.wait()
    print("Finished Listening.")
    write("audio.wav", fs, recording)
    print("Finished writing")
    segments, info = model.transcribe("audio.wav", beam_size=5)
    result = "".join([segment.text for segment in segments])
    print(f"[USER] {result}")
    return result

# Speak the response from the LLM
def speak(response_text, filename="response.wav"):
    print(f"[NOVA] {response_text}")
    #tts_model.tts_to_file(text=response_text, file_path=filename)
    engine.say(response_text)
    engine.runAndWait()
    #os.system(f"aplay {filename}" if os.name != 'nt' else f"start {filename}")

class Audio:
    def __init__(self, TTS_MODEL, STT_MODEL, signals):
        self.stt = pyttsx3.init()
        self.tts = WbisperModel(STT_MODEL, compute_type="int8")
    
    def listen(self):
        fs = 16000  # Whisper likes 16kHz mono
        seconds = 5
        print("Listening...")
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        time.sleep(5)
        sd.wait()
        print("Finished Listening.")
        write("audio.wav", fs, recording)
        print("Finished writing")
        segments, info = model.transcribe("audio.wav", beam_size=5)
        result = "".join([segment.text for segment in segments])
        print(f"[USER] {result}")
        return result
    
    def listen_loop(self):
        
        while True:
            

"""
# Adjust this port to match yours (likely /dev/ttyACM0 or /dev/ttyUSB0)
ser = serial.Serial('/dev/ttyACM0', 115200)

async def read_microbit():
    line = ser.readline().decode().strip()
    if line:
        try:
            x, y, z, tilt = line.split(",")
            x, y, z = int(x), int(y), int(z)
            print(f"Accel: x={x}, y={y}, z={z}, Tilt: {tilt}")
            return x, y, z, tilt
        except:
            print("NO RESPONSE FROM SERIAL INTERFACE")
"""
