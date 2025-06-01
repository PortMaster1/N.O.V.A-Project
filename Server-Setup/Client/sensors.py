import os, serial, time
from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3
import asyncio
import requests
from RealtimeSTT import AudioToTextRecorder


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



### Delete
def process_text(text):
    print(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder()

    while True:
        recorder.text(process_text)
### End Delete

class STT:
    def __init__(self, signals):
        self.recorder = None
        self.signals = signals
        self.API = self.API(self)
        self.enabled = True
    
    def process_text(self, text):
        if not self.enabled:
            return
        print("STT OUTPUT: " + text)
        self.signals.history.append({"role": "user", "content": tect})
        self.signals.last_message_time = time.time()
        if not self.signals.AI_speaking:
            self.signals.new_message = True
    
    def recording_start(self):
        self.signals.human_speaking = True

    def recording_stop(self):
        self.signals.human_speaking = False

    def feed_audio(self, data):
        self.recorder.feed_audio(data)


class STT:
    def __init__(self, signals):
        self.recorder = None
        self.signals = signals
        self.API = self.API(self)
        self.enabled = True

    def process_text(self, text):
        if not self.enabled:
            return

        print("STT OUTPUT: " + text)
        self.signals.history.append({"role": "user", "content": text})

        self.signals.last_message_time = time.time()
        if not self.signals.AI_speaking:
            self.signals.new_message = True

    def recording_start(self):
        self.signals.human_speaking = True

    def recording_stop(self):
        self.signals.human_speaking = False

    def feed_audio(self, data):
        self.recorder.feed_audio(data)

    def listen_loop(self):
        print("STT Starting")
        recorder_config = {
            'spinner': False,
            'language': 'en',
            'use_microphone': True,
            'input_device_index': INPUT_DEVICE_INDEX,
            'silero_sensitivity': 0.6,
            'silero_use_onnx': True,
            'post_speech_silence_duration': 0.4,
            'min_length_of_recording': 0,
            'min_gap_between_recordings': 0.2,
            'enable_realtime_transcription': True,
            'realtime_processing_pause': 0.2,
            'realtime_model_type': 'tiny.en',
            'compute_type': 'auto',
            'on_recording_start': self.recording_start,
            'on_recording_stop': self.recording_stop,
            'level': logging.ERROR
        }

        with AudioToTextRecorder(**recorder_config) as recorder:
            self.recorder = recorder
            print("STT Ready")
            self.signals.stt_ready = True
            while not self.signals.terminate:
                if not self.enabled:
                    time.sleep(0.2)
                    continue
                recorder.text(self.process_text)

    class API:
        def __init__(self, outer):
            self.outer = outer

        def set_STT_status(self, status):
            self.outer.enabled = status
            self.outer.signals.sio_queue.put(('STT_status', status))

        def get_STT_status(self):
            return self.outer.enabled

        def shutdown(self):
            self.outer.recorder.stop()
            self.outer.recorder.interrupt_stop_event.set()

### END CLASS

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
