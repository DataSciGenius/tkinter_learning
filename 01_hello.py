# Link: https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Create Graphical User Interfaces With Python And TKinter

# Importing the Tkinter library
from tkinter import Tk, Label

# Creating the main window (root widget)
root = Tk()
root.title("Create Graphical User Interfaces With Python And TKinter")

# Creating a Label widget with the text 'Hello World!'
mylabel = Label(root, text='Hello World!')

# Displaying the Label widget on the screen
mylabel.pack()

# Running the main event loop
root.mainloop()

# endregion
