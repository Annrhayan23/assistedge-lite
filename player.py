
import json, time, pyautogui

workflow = json.load(open("workflow.json"))

for step in workflow:
    if step["type"] == "click":
        x,y = step["position"]
        pyautogui.click(x,y)
    elif step["type"] == "key_press":
        pyautogui.press(step["key"])
    time.sleep(0.2)
