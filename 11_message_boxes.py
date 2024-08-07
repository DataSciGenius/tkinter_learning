# Link: https://youtu.be/S3AaSwpb5GE?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Message Boxes with TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image
from tkinter import messagebox

# Creating the main window (root widget)
root = Tk()
root.title("Message Boxes with TKinter")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion('This is my popup', 'Hello World!')
    Label(root, text=response).pack()

    if response == 'yes':
        Label(root, text='You clicked Yes!')
    else: Label(root, text='You clicked No!')

Button(root, text='Popup', command=popup).pack()

# Running the main event loop
root.mainloop()

# endregion