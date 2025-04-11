import speech_recognition as sr
import pyttsx3
import requests

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Adjust speed if needed

# REST API URL of your LLM server
SERVER_URL = "http://192.168.12.34:8000/chat"  # Update IP

# Speak function
def speak(text):
    print("Robot says:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "API unavailable"

# Talk to server
def talk_to_server(message):
    response = requests.post(SERVER_URL, json={"message": message})
    return response.json()["response"]

# Conversation loop
while True:
    user_input = listen()
    print("You said:", user_input)

    if "exit" in user_input.lower():
        speak("Goodbye, friend!")
        break

    reply = talk_to_server(user_input)
    speak(reply)