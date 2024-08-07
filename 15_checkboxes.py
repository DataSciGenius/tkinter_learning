# Link: https://youtu.be/4IsLwwb_yDs?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Checkboxes With TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("Checkboxes With TKinter")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')
# Setting the initial size of the window
root.geometry('400x400')

# Function to be called when the button is clicked
def show():
    # Creating a Label widget to display the current value of the variable
    my_label = Label(root, text=variable.get()).pack()

# Defining a StringVar variable to hold the value of the Checkbutton
variable = StringVar()
# Creating a Checkbutton widget with text and variable, setting onvalue and offvalue
checkbox = Checkbutton(root, text='Would you like to order Pizza or Hamburger?', variable=variable, onvalue='Pizza', offvalue='Hamburger')
# Deselecting the Checkbutton by default
checkbox.deselect()
# Displaying the Checkbutton widget on the screen
checkbox.pack()

# Creating a Button widget with the text 'Show selection!' and setting its command to the show function
my_button = Button(root, text='Show selection!', command=show).pack()

# Running the main event loop
root.mainloop()


# endregion