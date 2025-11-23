

# AssistEdge Lite – RPA Bot

**Automate repetitive tasks on your desktop with Python and PyAutoGUI.**

## Overview

AssistEdge Lite is a lightweight RPA (Robotic Process Automation) bot built with Python. It reads a workflow defined in a JSON file and executes mouse clicks and keyboard actions automatically. Perfect for automating repetitive tasks like data entry, form filling, or testing.

---

## Features

* Reads a JSON-based workflow (`workflow.json`) to define automation steps.
* Supports mouse clicks at specific screen coordinates.
* Supports keyboard key presses (Enter, Tab, Space, etc.).
* Safe loading with a fallback default workflow if JSON is missing.
* Real-time console output for every action executed.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Annrhayan23/assistedge-lite
cd assistedge-lite
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate   # macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> **Dependencies**: `pyautogui`, `streamlit`

---

## Usage

1. Make sure `workflow.json` exists in the project folder with the desired steps. Example:

```json
[
  {"type": "click", "position": [500, 300]},
  {"type": "key_press", "key": "enter"}
]
```

2. Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

3. Open the URL in your browser (`http://localhost:8501`) and your bot will execute the workflow.

---

## File Structure

```
assistedge-lite/
├── dashboard.py        # Streamlit UI
├── player.py           # RPA bot script
├── workflow.json       # JSON workflow file
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## How it Works

1. `player.py` loads `workflow.json`.
2. Each step has a `type` (`click` or `key_press`) and required parameters (`position` or `key`).
3. The bot executes each step in sequence with a short delay.
4. If `workflow.json` is missing or invalid, a default workflow runs instead.

---

## Notes

* Make sure the screen resolution matches the coordinates in the JSON.
* Run with admin privileges if automating apps that require it.
* Use responsibly — this simulates mouse and keyboard events on your system.

---

## GitHub

[https://github.com/Annrhayan23/assistedge-lite](https://github.com/Annrhayan23/assistedge-lite)

---

I can also make a **shorter, LinkedIn-friendly version** of this README that’s punchy and highlights the project in a few lines.

Do you want me to do that too?
