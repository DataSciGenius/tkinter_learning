# Link: https://youtu.be/uqJZWLlnSqs?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Radio Buttons with TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image

# Creating the main window (root widget)
root = Tk()
root.title("Radio Buttons with TKinter")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# Defining an IntVar variable and setting its default value to '2'
# variable = IntVar()
# variable.set('2')

# List of pizza toppings for the Radiobuttons
toppings = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

# Defining a StringVar variable for the selected pizza topping and setting its default value to 'Pepperoni'
pizza = StringVar()
pizza.set('Pepperoni')

# Creating Radiobuttons for each topping in the toppings list
for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

# Function to be called when the button is clicked
def clicked(value):
    # Creating a Label widget to display the selected topping
    my_label = Label(root, text=value)
    # Displaying the Label widget on the screen
    my_label.pack()

# Radiobutton(root, text='Option 1', variable=variable, value=1, command=lambda: clicked(variable.get())).pack()
# Radiobutton(root, text='Option 2', variable=variable, value=2, command=lambda: clicked(variable.get())).pack()

# my_label = Label(root, text=pizza.get())
# my_label.pack()

# Creating a Button widget with the text 'Click me!' and setting its command to the clicked function
# The command passes the currently selected topping to the clicked function
my_button = Button(root, text='Click me!', command=lambda: clicked(pizza.get()))
# Displaying the Button widget on the screen
my_button.pack()

# Running the main event loop
root.mainloop()

# endregion