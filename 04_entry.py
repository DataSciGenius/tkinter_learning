# Link: https://www.youtube.com/watch?v=7A_csP9drJw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=4

# region Creating Input Fields With TKinter

# Importing the Tkinter library
from tkinter import *

# Creating the main window (root widget)
root = Tk()
root.title("reating Input Fields With TKinter")

# Creating an Entry widget with a specified width, background color, foreground color, and border width
entry = Entry(root, width=50, bg='black', fg='white', borderwidth=5)
# Displaying the Entry widget on the screen
entry.pack()
# Inserting the initial text "Enter Your Name: " into the Entry widget
entry.insert(0, "Enter Your Name: ")

# Defining the function that will be executed when the button is clicked
def myclick():
    # Retrieving the text from the Entry widget and forming a greeting message
    hello = f'Hello {entry.get()}'
    # Creating a Label widget with the greeting message
    mylabel = Label(root, text=hello)
    # Displaying the Label widget on the screen
    mylabel.pack()

# Creating a Button widget with the text 'Enter Your Name' and setting its command to the myclick function
mybutton = Button(root, text='Enter Your Name', command=myclick)

# Displaying the Button widget on the screen
mybutton.pack()

# Running the main event loop
root.mainloop()


# endregion