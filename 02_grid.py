# Link: https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2

# region Positioning With Tkinter's Grid System

# Importing the Tkinter library
from tkinter import *

# Creating the main window (root widget)
root = Tk()
root.title("Positioning With Tkinter's Grid System")

# Creating Label widgets with various texts
mylabel1 = Label(root, text='Hello World!')
mylabel2 = Label(root, text='My name is Mustafa.')
mylabel3 = Label(root, text='                       ')

# Displaying the Label widgets on the screen using grid layout
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=2)
mylabel3.grid(row=1, column=1)

# Running the main event loop
root.mainloop()

# endregion