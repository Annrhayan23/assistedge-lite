
import mouse, keyboard, json, time, pyautogui

actions = []

def on_click(event):
    actions.append({
        "type": "click",
        "button": event.button,
        "position": mouse.get_position(),
        "timestamp": time.time()
    })

def on_key(event):
    actions.append({
        "type": "key_press",
        "key": event.name,
        "timestamp": time.time()
    })

mouse.on_click(on_click)
keyboard.on_press(on_key)

print("Recording... Press ESC to stop.")
keyboard.wait("esc")

with open("workflow.json","w") as f:
    json.dump(actions,f,indent=4)
print("Saved to workflow.json")
