import keyboard, threading, json
from os import system

# Define the hotkey
keyboard.add_hotkey('ctrl+left windows+alt+p', lambda: on_hotkey())

# Define the function that gets called when the hotkey is triggered
def on_hotkey():
    print("Hotkey triggered!")
    t = threading.Thread(target=record_keystrokes)
    t.start()


def record_keystrokes():
    print("Recording...")
    # Record keystrokes until Enter is pressed
    recorded = keyboard.record(until='enter')
    crosshair = ''.join([key.name for key in recorded if key.event_type == 'down' and key.name != 'enter'])
    try:
        file = open('crosshairs.json')
        crosshairs = json.load(file)
        system(f'echo {crosshairs[crosshair]} | clip')
    except KeyError:
        pass


# Start the keyboard listener
keyboard.wait()