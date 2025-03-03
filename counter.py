import threading
from pynput import keyboard, mouse
from datetime import datetime

ctrl_count = 0
click_count = 0
start_time = datetime.now()
running = True

def on_press(key):
    global ctrl_count, running
    if key == keyboard.Key.ctrl_l:
        ctrl_count += 1
        print(f"Ctrl gauche pressé {ctrl_count} fois")

def on_click(x, y, button, pressed):
    global click_count
    if button == mouse.Button.left and pressed:
        click_count += 1
        print(f"Clic gauche effectué {click_count} fois")

def stop_listener():
    global running
    while running:
        command = input()
        if command.lower() == "stop":
            running = False

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

stop_thread = threading.Thread(target=stop_listener)
stop_thread.start()

while running:
    pass

end_time = datetime.now()

with open("journalier.txt", "a", encoding="utf-8") as file:
    file.write(f"\nDate : {start_time.strftime('%d/%m/%Y')}\n")
    file.write(f"Heure de début : {start_time.strftime('%H:%M:%S')}\n")
    file.write(f"Heure de fin : {end_time.strftime('%H:%M:%S')}\n")
    file.write(f"Nombre de Ctrl gauche pressés : {ctrl_count}\n")
    file.write(f"Nombre de clics gauches : {click_count}\n")
    file.write("-" * 30 + "\n")

print("Données enregistrées dans journalier.txt ✅")
