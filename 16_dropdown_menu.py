# Link: https://youtu.be/3E_fK5hCUnI?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Dropdown Menus With TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("Dropdown Menus With TKinter")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')
# Setting the initial size of the window
root.geometry('400x400')

# Function to be called when the button is clicked
def show():
    # Creating a Label widget to display the current value of the clicked variable
    my_label = Label(root, text=clicked.get()).pack()

# List of options for the dropdown menu
options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Defining a StringVar variable to hold the value of the selected option
clicked = StringVar()
# Setting the default value of the dropdown menu to the first option in the list
clicked.set(options[0])

# Creating an OptionMenu widget with the list of options and the clicked variable
dropdown = OptionMenu(root, clicked, *options)
# Displaying the OptionMenu widget on the screen
dropdown.pack()

# Creating a Button widget with the text 'Show selection' and setting its command to the show function
my_button = Button(root, text='Show selection', command=show).pack()

# Running the main event loop
root.mainloop()

# endregion