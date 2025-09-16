# vision.py
from picamera2 import Picamera2
import cv2
import face_recognition
from speech_io import speak
import threading
import time

# Initialize Pi Camera 3
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "XRGB8888", "size": (640, 480)}))
picam2.start()

person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

known_face_encodings = []
known_face_names = []

alex_image = face_recognition.load_image_file("../images/alex.jpg")
alex_encoding = face_recognition.face_encodings(alex_image)[0]
known_face_encodings.append(alex_encoding)
known_face_names.append("Alex")

def greet_person(name):
    if name == "Alex":
        speak("Hello Alex! I am your robot.")
    else:
        speak("আসসালামু আলাইকুম")

def person_detection():
    while True:
        frame = picam2.capture_array()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        persons = person_cascade.detectMultiScale(gray, 1.1, 4)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            greet_person(name)
            time.sleep(5)

        if len(persons) > 0 and len(face_encodings) == 0:
            greet_person("Unknown")
            time.sleep(5)

threading.Thread(target=person_detection, daemon=True).start()
