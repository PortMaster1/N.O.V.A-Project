import socket
from ultralytics import YOLO
import cv2
import time

# Socket setup
HOST = '192.168.100.1'  # IP of Orin A (Nova's brain)
PORT = 65432

# YOLO model setup
model = YOLO("yolov8n.pt")  # Use YOLOv8 nano for speed

# Camera setup (0 for USB webcam or CSI camera)
cap = cv2.VideoCapture(0)

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Run detection
    results = model(frame)
    objects = set()

    for result in results:
        for name in result.names.values():
            objects.add(name)

    # Create summary
    if objects:
        summary = f"Nova sees: {', '.join(objects)}."
    else:
        summary = "Nova sees nothing interesting."

    # Send to LLM server
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(summary.encode())
    except Exception as e:
        print("Error sending to brain:", e)

    time.sleep(1)  # Add a small delay to avoid overloading the server