# Link: https://youtu.be/YR3h2CY21-U?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Using Databases With TKinter

# Importing the Tkinter library
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library
from PIL import ImageTk, Image
# Importing the sqlite3 library to work with SQLite databases
import sqlite3

# Creating the main window (root widget)
root = Tk()
root.title("Using Databases With TKinter")
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')
# Setting the initial size of the window
root.geometry('400x400')

# Connecting to the SQLite database (or creating it if it doesn't exist)
connection = sqlite3.connect('address_book.db')

# Creating a cursor object to execute SQL commands
cursor = connection.cursor()

# Executing an SQL command to create a table if it doesn't already exist
cursor.execute("""
    CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )  
""")

# Committing the changes to the database
connection.commit()

# Closing the connection to the database
connection.close()

# Running the main event loop
root.mainloop()

# endregion