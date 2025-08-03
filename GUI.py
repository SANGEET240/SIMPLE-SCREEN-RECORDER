from tkinter import *
from PIL import Image, ImageTk
from recorder import *
from threading import Thread


is_recording = True

def toggle():
    global is_recording
    if is_recording:
        record_button.config(image = stop_image)
        Thread(target=start_recording, daemon=True).start()
        is_recording = False
    else:
        record_button.config(image = start_image)
        stop_recording()
        is_recording = True
        
# ----------------------WINDOW OBJECT CREATION--------------------------------

window = Tk()

# --------------------WINDOW TITLE, ICON, BACKGROUND--------------------------

window.geometry("400x60")
window.title("Screen recorder by SANGEET")
window.resizable(False, False)
window.pack_propagate(False)
window.update_idletasks()
window.minsize(400, 60)
window.maxsize(400, 60)

icon = PhotoImage(file = "C:\\Users\\SANGEET\\OneDrive\\Desktop\\Screen recorder project\\title_logo.png")
window.iconphoto(True, icon)

image = Image.open("C:\\Users\\SANGEET\\OneDrive\\Desktop\\Screen recorder project\\bg.png")
image = image.resize((400, 60))
bg_image = ImageTk.PhotoImage(image)

background = Label(window, image=bg_image)
background.place(x = 0, y = 0, relwidth=1, relheight=1)

# ------------------------START/STOP RECORD BUTTON-----------------------------

image = Image.open("C:\\Users\\SANGEET\\OneDrive\\Desktop\\Screen recorder project\\start_record.png")
image = image.resize((150, 30))
start_image = ImageTk.PhotoImage(image)

image = Image.open("C:\\Users\\SANGEET\\OneDrive\\Desktop\\Screen recorder project\\stop_record.png")
image = image.resize((150, 30))
stop_image = ImageTk.PhotoImage(image)

record_button = Button(window,
                       image = start_image,
                       background = 'black',
                       activebackground = '#373737',
                       command = toggle)
record_button.place(x = 30, y = 12)

window.mainloop()