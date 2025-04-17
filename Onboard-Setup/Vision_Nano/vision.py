import asyncio
import time
from ultralytics import YOLO
from deepface import DeepFace

import requests
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image, get_object



# Globals
detected_faces = []
frame_lock = threading.Lock()
result_lock = threading.Lock()
latest_results = {}

# Load models
yolo = YOLO("yolov8n.pt")  # or yolov8s.pt for more accuracy
known_face_encodings = []  # Load your known faces here
known_face_names = []
model = insightface.app.FaceAnalysis(name='buffalo_l')
model.prepare(ctx_id=0)  # Set to 0 for GPU, -1 for CPU

# Read an image
img = cv2.imread("test.jpg")

# Detect faces
faces = model.get(img)

for face in faces:
    print("Detected face with embedding:", face.embedding)

# TODO: Fix this v
# WebSocket or REST endpoint
SERVER_URL = "http://your-nova-brain-ip:8000/api/input"

# Motion Detector Setup
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

async def object_detection_thread(camera_index=0):
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        results = yolo(frame)
        people = []

        for det in results[0].boxes.data:
            class_id = int(det[5])
            if class_id == 0:  # Person
                x1, y1, x2, y2 = map(int, det[:4])
                people.append(frame[y1:y2, x1:x2])

        with frame_lock:
            detected_faces.clear()
            detected_faces.extend(people)

        asyncio.sleep(0.1)

async def motion_tracking_thread(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        motion_mask = bg_subtractor.apply(frame)
        motion_area = np.sum(motion_mask > 0)
        if motion_area > 5000:  # Tune this threshold
            print("[Motion] Movement Detected")
        asyncio.sleep(0.2)

async def face_analysis_thread():
    while True:
        with frame_lock:
            faces = detected_faces.copy()
        for face in faces:
            try:
                analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)[0]
                emotion = analysis["dominant_emotion"]
                print("[Emotion] Detected:", emotion)

                # Face Recognition
                rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                encodings = face_recognition.face_encodings(rgb)
                name = "Unknown"
                if encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, encodings[0])
                    if True in matches:
                        name = known_face_names[matches.index(True)]
                
                with result_lock:
                    latest_results["emotion"] = emotion
                    latest_results["face"] = name

            except Exception as e:
                print("[DeepFace] Error:", e)

        asyncio.sleep(1)  # Run at most once per second

async def send_results_thread():
    while True:
        with result_lock:
            data = latest_results.copy()
        if data:
            try:
                response = requests.post(SERVER_URL, json=data)
                print("[Send] Data sent:", data)
            except Exception as e:
                print("[Send] Error:", e)
        asyncio.sleep(1)

# Launch threads
asyncio.run(target=object_detection_thread)
asyncio.run(target=motion_tracking_thread)
asyncio.run(target=face_analysis_thread)
asyncio.run(target=send_results_thread)

# Keep the main thread alive
while True:
    asyncio.sleep(10)