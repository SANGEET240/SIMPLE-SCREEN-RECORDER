import cv2
import numpy as np
import mss
import os
import shutil
from tkinter import filedialog

start = False
out = None  # Will store VideoWriter object
temp_filename = "temp_record.avi"  # Temporary file

def start_recording(width=1920, height=1080, fps=20.0):
    global start, out
    start = True

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(temp_filename, fourcc, fps, (width, height))

    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": width, "height": height}

        print("Recording started...")
        while start:
            img = sct.grab(monitor)
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            out.write(frame)

    out.release()
    cv2.destroyAllWindows()
    print("Recording stopped.")

def stop_recording():
    global start, out, temp_filename
    start = False

    if out is not None:
        # Ask user where to save the file
        save_path = filedialog.asksaveasfilename(
            defaultextension=".avi",
            filetypes=[("AVI files", "*.avi"), ("All files", "*.*")],
            title="Save Recording As"
        )

        if save_path:
            shutil.move(temp_filename, save_path)
            print(f"Recording saved as: {save_path}")
        else:
            # If user cancels save, delete temp file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
            print("Recording discarded.")
