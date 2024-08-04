# Link: https://www.youtube.com/watch?v=yuuDJ3-EdNQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=3

# region Creating Buttons With TKinter

# Importing the Tkinter library
from tkinter import *

# Creating the main window (root widget)
root = Tk()

# Defining the function that will be executed when the button is clicked
def myclick():
    # Creating a Label widget with the text 'Look! I clicked a Button!'
    mylabel = Label(root, text='Look! I clicked a Button!')
    # Displaying the Label widget on the screen
    mylabel.pack()

# Creating a Button widget with the text 'Click me!' and setting its state to DISABLED
# mybutton = Button(root, text='Click me!', state=DISABLED)   # state=DISABLED makes unclickable the button

# Creating a Button widget with the text 'Click me!' and setting its horizontal padding (padx) and vertical padding to 50 and 25, respectively
# mybutton = Button(root, text='Click me!', padx=50, pady=25, command=myclick)

# Creating a Button widget with the text 'Click me!', setting its command to the myclick function, and customizing its foreground color (text color) to blue and background color to green
mybutton = Button(root, text='Click me!', command=myclick, fg='blue', bg='green')
# mybutton = Button(root, text='Click me!', command=myclick, fg='blue', bg='#000000')     # can be used hex color code like '#000000', as well

# The issue with command=myclick() is that it calls the myclick function immediately during the creation of the Button widget, rather than passing the function itself to be called when the button is clicked. This happens because adding parentheses () to the function name executes the function immediately.
# mybutton = Button(root, text='Click me!', command=myclick())


# Displaying the Button widget on the screen
mybutton.pack()

# Running the main event loop
root.mainloop()

# endregion