# Link: https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Create Graphical User Interfaces With Python And TKinter

# Importing the Tkinter library
from tkinter import Tk, Label

# Creating the main window (root widget)
root = Tk()  # Initialize the main application window
# Setting the title of the window
root.title("Hello World!")
# Setting the initial size of the window
root.geometry('300x200')  # Width x Height in pixels

# Creating a Label widget with the text 'Hello World!'
mylabel = Label(root, text='Hello World!')

# Displaying the Label widget on the screen
mylabel.pack()

# Running the main event loop
root.mainloop()

# endregion
