# 🔒 faceLock

A simple face-based screen locker for Linux.

This app runs in the background and automatically locks your screen if **no face is detected** for a specified period after login. It uses your webcam and OpenCV to detect presence — later, it can be extended to recognize *your specific face*.

---

## 🧠 How It Works

1. Waits **1 minute after login unlock**.
2. Starts monitoring the webcam for a face.
3. If **no face is detected for 1 minute**, it automatically **locks the screen**.
4. Monitoring stops after locking.
5. Resumes after next unlock.

---

## 📦 Features

- ⏳ Post-login delay
- 🧍 Face detection (OpenCV)
- 🔒 Session lock integration (via `loginctl`)
- 🖥️ D-Bus event listener (real-time unlock monitoring)
- 🧰 Modular structure, easy to extend with face recognition

---

## 🗂️ Project Structure

faceLock/ 
├── main.py # App entry point and logic 
├── session_monitor.py # Listens for session unlock via D-Bus 
├── face_monitor.py # Handles face detection via webcam 
├── locker.py # Locks screen using loginctl 
├── config.py # Timing and constants 
├── requirements.txt # Python packages (pip-installable) 
└── README.md


---

## 🛠️ Requirements

### ✅ System Packages (for D-Bus and GObject)
Install these using APT:

```bash
sudo apt update
sudo apt install python3-dbus python3-gi libglib2.0-dev libdbus-1-dev

✅ Python Environment (Recommended: Python 3.12 + venv)

Create a virtual environment with system package access:

python3.12 -m venv .venv --system-site-packages
source .venv/bin/activate

Install Python packages:

pip install opencv-python
