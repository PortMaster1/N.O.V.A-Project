import os, serial
from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
from TTS.api import TTS

# Initialize STT and TTS Engines
model = WhisperModel("base.en", compute_type="int8")  # Use "tiny", "base", or "small" for speed
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# Listen function
def listen():
    fs = 16000  # Whisper likes 16kHz mono
    seconds = 5
    print("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write("audio.wav", fs, recording)
    segments, info = model.transcribe("audio.wav", beam_size=5)
    result = "".join([segment.text for segment in segments])
    print(f"[USER] {result}")
    return result

# Speak the response from the LLM
def speak_response(response_text, filename="response.wav"):
    print(f"[NOVA] {response_text}")
    tts_model.tts_to_file(text=response_text, file_path=filename)
    os.system(f"aplay {filename}" if os.name != 'nt' else f"start {filename}")

# Adjust this port to match yours (likely /dev/ttyACM0 or /dev/ttyUSB0)
ser = serial.Serial('/dev/ttyACM0', 115200)

def read_microbit():
    while True:
        line = ser.readline().decode().strip()
        if line:
            try:
                x, y, z, tilt = line.split(",")
                x, y, z = int(x), int(y), int(z)
                print(f"Accel: x={x}, y={y}, z={z}, Tilt: {tilt}")
                return x, y, z, tilt
            except:
                print("NO RESPONSE FROM SERIAL INTERFACE")