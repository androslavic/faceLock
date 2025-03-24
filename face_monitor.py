import cv2
import time
from config import CAMERA_INDEX

class FaceMonitor:
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def face_detected(self):
        ret, frame = self.cap.read()
        if not ret:
            return False
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return len(faces) > 0

    def release(self):
        self.cap.release()
