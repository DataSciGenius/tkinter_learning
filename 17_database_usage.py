# Link 1: https://youtu.be/YR3h2CY21-U?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 2: https://youtu.be/AK1J8xF4fuk?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Using Databases With TKinter, Building Out The GUI for our Database App

# Importing the Tkinter library for creating GUI applications
from tkinter import *
# Importing the Image and ImageTk classes from the PIL (Pillow) library for handling images
from PIL import ImageTk, Image
# Importing the sqlite3 library to work with SQLite databases
import sqlite3

# Creating the main window (root widget)
root = Tk()
root.title("Using Databases With TKinter")  # Setting the title of the window
# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')
# Setting the initial size of the window
root.geometry('400x400')

# Create submit function for database
def submit():
    # Connecting to the SQLite database (or creating it if it doesn't exist)
    connection = sqlite3.connect('address_book.db')
    # Creating a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Insert the data from the text boxes into the addresses table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {
                       'f_name': f_name.get(),       # Fetching the first name from the text box
                       'l_name': l_name.get(),       # Fetching the last name from the text box
                       'address': address.get(),     # Fetching the address from the text box
                       'city': city.get(),           # Fetching the city from the text box
                       'state': state.get(),         # Fetching the state from the text box
                       'zipcode': zipcode.get()      # Fetching the zipcode from the text box
                   })

    # Committing the changes to the database
    connection.commit()
    # Closing the connection to the database
    connection.close()

    # Clearing the text boxes after submission
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create a query function to retrieve and display records from the database
def query():
    # Connecting to the SQLite database (or creating it if it doesn't exist)
    connection = sqlite3.connect('address_book.db')
    # Creating a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Query the database to retrieve all records from the addresses table
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()  # Fetching all the records
    # print(records)

    # Prepare the data for display
    print_records = ''
    for record in records:
        print_records += f'{record[0]}, {record[1]}, {record[2]}, {record[3]}, {record[4]}, {record[5]} \n'

    # Create a label widget to display the records
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Committing the changes to the database
    connection.commit()
    # Closing the connection to the database
    connection.close()

# Create text boxes for user input
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)  # Positioning the text box

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create labels for each text box to indicate what information should be entered
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State')
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

# Create a button to submit the entered data to the database
submit_button = Button(root, text='Add record to database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a button to query and display records from the database
query_button = Button(root, text='Show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Running the main event loop to keep the application window open
root.mainloop()


# endregion