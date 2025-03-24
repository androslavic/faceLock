import os

def lock_screen():
    print("🔒 Locking screen...")
    os.system("loginctl lock-session")
