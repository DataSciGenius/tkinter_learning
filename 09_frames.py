# Link: https://youtu.be/_auZ8TTkojQ?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Adding Frames To Your Program

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("Adding Frames To Your Program")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# Creating a frame with padding inside the main window
frame = LabelFrame(root, padx=20, pady=20)
# Displaying the frame on the screen with additional padding
frame.pack(padx=10, pady=10)

# Creating two buttons within the frame
button1 = Button(frame, text="Don't click here!")
button2 = Button(frame, text="Click here!")
# Placing the first button in the first row and first column of the grid within the frame
button1.grid(row=0, column=0)
# Placing the second button in the second row and first column of the grid within the frame
button2.grid(row=1, column=0)

# Running the main event loop
root.mainloop()


# endregion