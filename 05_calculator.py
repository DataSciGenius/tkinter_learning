# Link 1: https://youtu.be/F5PfbC5ld-Q?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 2: https://youtu.be/XhCfsuMyhXo?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 3: https://youtu.be/oq3lJdhnPp8?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Building A Simple Calculator App

# Importing the Tkinter library
from tkinter import *

# Creating the main window (root widget)
root = Tk()
root.title("Building A Simple Calculator App")

# Creating an Entry widget for the calculator display with specified width and border width
entry = Entry(root, width=35, borderwidth=5)
# Placing the Entry widget in the grid
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function to handle button clicks for numbers
def button_click(number):
    current = entry.get()  # Get the current text in the Entry widget
    entry.delete(0, END)  # Clear the Entry widget
    entry.insert(0, str(current) + str(number))  # Insert the new number

# Function to clear the Entry widget
def button_clear():
    entry.delete(0, END)

# Function to handle the addition operation
def button_add():
    first_number = entry.get()  # Get the first number
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to handle the subtraction operation
def button_subtract():
    first_number = entry.get()  # Get the first number
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to handle the multiplication operation
def button_multiply():
    first_number = entry.get()  # Get the first number
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to handle the division operation
def button_divide():
    first_number = entry.get()  # Get the first number
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

# Function to handle the equals operation
def button_equal():
    second_number = entry.get()  # Get the second number
    entry.delete(0, END)

    # Perform the appropriate operation based on the math variable
    if math == 'addition':
        entry.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        entry.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        entry.insert(0, f_num * int(second_number))
    elif math == 'division':
        entry.insert(0, f_num / int(second_number))

# Creating the calculator buttons with their text, padding, and command
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text='x', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text='/', padx=41, pady=20, command=button_divide)

button_equal = Button(root, text='=', padx=89, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=button_clear)

# Placing the buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Running the main event loop
root.mainloop()

# endregion