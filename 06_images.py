# Link: https://youtu.be/NoTM8JciWaQ?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Using Icons, Images, and Exit Buttons

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("Simple Calculator")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# Loading an image from a file and creating an ImageTk object
my_img = ImageTk.PhotoImage(Image.open('images/world.jpg'))
# Creating a Label widget to display the image
my_label = Label(image=my_img, width=1000, height=800)
# Displaying the Label widget on the screen
my_label.pack()

# Creating a Button widget to exit the program
button_exit = Button(root, text='Exit Program', command=root.quit)
# Displaying the Button widget on the screen
button_exit.pack()

# Running the main event loop
root.mainloop()

# endregion