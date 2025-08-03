# 🖥️ Screen Recorder by Sangeet

A lightweight screen recording application with a custom-designed GUI using **Tkinter** and **OpenCV**. This project allows users to record their screen with a simple click of a "Start Recording" button, and stop it with another click, while also letting them choose where and under what name to save the recording.

---

## 🚀 Features

- 🎬 Start and Stop screen recording with a single button
- 🖼️ Custom GUI with background image and styled buttons
- 💾 Save the video with a custom file name and location
- 📼 Output format: `.avi` (XVID codec)
- 🧵 Uses threading to prevent GUI freezing
- 📷 Captures full HD screen using `mss`

---

## 📁 Project Structure
Screen-Recorder-Project/

│

├── screen_gui.py # GUI code using Tkinter

├── recorder.py # Core recording logic (OpenCV + MSS)

│

├── start_record.png # Start button image

├── stop_record.png # Stop button image

├── bg.png # Background image for GUI

└── title_logo.png # Window icon

---

## 🛠️ Requirements

- Python 3.x
- `opencv-python`
- `mss`
- `Pillow` (for image handling in GUI)

---
## 🔧 How It Works  

The screen_gui.py file creates a fixed-size GUI window with styled buttons and background.
Pressing Start Recording launches start_recording() from recorder.py using a background thread.
Pressing Stop Recording stops the capture and prompts the user to save the file using a save dialog box.
The screen capture is done using mss, and video encoding is handled by OpenCV's VideoWriter.

## 📸 Output  

Format: .avi (XVID codec)
Resolution: 1920x1080 (modifiable in recorder.py)
Frame rate: 30 FPS
Saved using user-defined file name and location

## 👤 Author<br>
Made by Sangeet

Install dependencies:
```bash 
pip install opencv-python mss Pillow