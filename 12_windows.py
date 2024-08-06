# Link: https://youtu.be/qC3FYdpJI5Y?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Create New Windows in TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("My First Window")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# Function to open a new window
def open():
    global my_image
    # Creating a new top-level window
    top = Toplevel()
    top.title("My Second Window")
    # Setting the window icon for the second window (ensure the path to the icon is correct)
    top.iconbitmap(r'C:\Users\musta\tkinter_project')
    # Loading an image from a file and creating an ImageTk object
    my_image = ImageTk.PhotoImage(Image.open('images/animal1.jpeg'))
    # Creating a Label widget to display the image in the second window
    my_label = Label(top, image=my_image).pack()
    # Creating a Button widget to close the second window
    button2 = Button(top, text='Close Window', command=top.destroy).pack()

# Creating a Button widget in the main window to open the second window
button = Button(root, text='Open Second Window', command=open).pack()

# Running the main event loop
root.mainloop()

# endregion