# Link: https://youtu.be/zg4c92pNFeo?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Build an Image Viewer App With Python and TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("Image Viewer")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# Loading images from files and creating ImageTk objects
my_img1 = ImageTk.PhotoImage(Image.open('images/animal1.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/animal2.jpeg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/animal3.jpeg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/animal4.jpeg'))
my_img5 = ImageTk.PhotoImage(Image.open('images/animal5.jpeg'))

# Creating a list of images
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Creating a Label widget to display the first image
my_label = Label(image=my_img1)
# Displaying the Label widget on the screen
my_label.grid(row=0, column=0, columnspan=3)

# Function to move forward through the image list
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Removing the current image
    my_label.grid_forget()
    # Updating the label with the next image
    my_label = Label(image=image_list[image_number - 1])
    # Updating the forward and back buttons
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    # Disabling the forward button if on the last image
    if image_number == 5:
        button_forward = Button(root, text='>>', state=DISABLED)

    # Displaying the new image and updated buttons
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Function to move backward through the image list
def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Removing the current image
    my_label.grid_forget()
    # Updating the label with the previous image
    my_label = Label(image=image_list[image_number - 1])
    # Updating the forward and back buttons
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    # Disabling the back button if on the first image
    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    # Displaying the new image and updated buttons
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Creating the initial navigation buttons
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

# Displaying the navigation buttons on the screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# Running the main event loop
root.mainloop()

# endregion