import threading
import time
from session_monitor import SessionMonitor
from face_monitor import FaceMonitor
from locker import lock_screen
from config import POST_LOGIN_DELAY, NO_FACE_TIMEOUT

monitoring = False

def start_face_monitoring():
    global monitoring
    if monitoring:
        return  # Avoid double monitoring
    monitoring = True
    print(f"⏳ Waiting {POST_LOGIN_DELAY}s after unlock...")
    time.sleep(POST_LOGIN_DELAY)

    face_monitor = FaceMonitor()
    print("🧠 Started face monitoring...")

    no_face_start = time.time()
    try:
        while True:
            if face_monitor.face_detected():
                print("🙂 Face detected.")
                no_face_start = time.time()
            elif time.time() - no_face_start >= NO_FACE_TIMEOUT:
                lock_screen()
                break
            time.sleep(1)
    finally:
        face_monitor.release()
        monitoring = False

def main():
    session = SessionMonitor(on_unlock_callback=lambda: threading.Thread(target=start_face_monitoring, daemon=True).start())
    session.start()

if __name__ == "__main__":
    main()
