# Link: https://youtu.be/Aim_7fC-inw?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Open Files Dialog Box

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

# Opening a file dialog to select a file and storing the file path in root.filename1
root.filename1 = filedialog.askopenfilename(initialdir=r'C:\Users\musta\tkinter_project\datasets',
                                            title='Select a File',
                                            filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
# Creating a Label widget to display the selected file path in the main window
my_label = Label(root, text=root.filename1).pack()

# Function to open a file dialog to select an image file
def open():
    global my_image
    # Opening a file dialog to select an image file and storing the file path in root.filename2
    root.filename2 = filedialog.askopenfilename(initialdir=r'C:\Users\musta\tkinter_project\images',
                                                title='Select a File',
                                                filetypes=(('jpg files', '*.jpeg'), ('all files', '*.*')))
    # Creating a Label widget to display the selected file path in the main window
    my_label = Label(root, text=root.filename2).pack()
    # Loading the selected image and creating an ImageTk object
    my_image = ImageTk.PhotoImage(Image.open(root.filename2))
    # Creating a Label widget to display the image in the main window
    my_image_label = Label(image=my_image).pack()

# Creating a Button widget to open the file dialog for selecting an image file
my_button = Button(root, text='Open File', command=open).pack()

# Running the main event loop
root.mainloop()

# endregion