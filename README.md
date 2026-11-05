# fetch-crosshair

A tiny Windows background script that copies a saved game crosshair code (written for Valorant) to the clipboard when you type its name after a global hotkey.

## How it works
1. Press `Ctrl + Left Win + Alt + P`.
2. Type the name of a crosshair and press Enter.
3. If `crosshairs.json` has an entry with that name, its value is copied to the clipboard (via `clip`); unknown names are ignored.

## Requirements
- Windows (uses `clip`)
- Python 3 and `pip install keyboard`. The `keyboard` library hooks global key events, which can require administrator rights.

## Setup
Create `crosshairs.json` next to `main.py`, mapping the name you will type to the crosshair code (not included in this repo):
```json
{
  "mycrosshair": "0;P;c;5;h;0;m;1;0l;4;0o;2;0a;1;0f;0;1b;0"
}
```
Names are matched against the individual key names you press, so keep them simple lowercase letters and digits.

## Run
```bash
python main.py
```
To start it without a console window, edit the paths in `run.bat` and use it. It launches `main.py` through `Quiet.exe`, a small third-party freeware utility by Joe Richards (joeware) that runs a command hidden; it is not part of this project.

## Limitations
Hobby script: it reads `crosshairs.json` on every lookup, doesn't report errors for a missing file, and has no tests.
