# Link: https://youtu.be/knUHd8ZGyiM?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Sliders With TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image
# Importing the filedialog module from Tkinter
from tkinter import filedialog

# Creating the main window (root widget)
root = Tk()
root.title("My First Window")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')
# Setting the initial size of the window
root.geometry('400x400')

# Creating a vertical Scale widget with a range from 0 to 200
vertical = Scale(root, from_=0, to=200)
# Displaying the vertical Scale widget on the screen
vertical.pack()

# Function to be called when the button is clicked
def slide():
    # Creating a Label widget to display the current value of the vertical scale
    my_label1 = Label(root, text=vertical.get()).pack()
    # Creating a Label widget to display the current value of the horizontal scale
    my_label2 = Label(root, text=horizontal.get()).pack()
    # Setting the window size to the current values of the horizontal and vertical scales
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    # Setting the window size to the current values of the vertical and horizontal scales
    root.geometry(str(vertical.get()) + "x" + str(horizontal.get()))

# Creating a horizontal Scale widget with a range from 0 to 400
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
# Displaying the horizontal Scale widget on the screen
horizontal.pack()

# Creating a Button widget with the text 'Click me!' and setting its command to the slide function
my_button = Button(root, text='Click me!', command=slide).pack()

# Running the main event loop
root.mainloop()

# endregion