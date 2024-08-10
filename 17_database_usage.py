# Link 1: https://youtu.be/YR3h2CY21-U?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 2: https://youtu.be/AK1J8xF4fuk?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 3: https://youtu.be/c9_gcIeAru0?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 4: https://youtu.be/EAs3gr9mC9g?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 5: https://youtu.be/0Ms0-68IgTY?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Using Databases With TKinter, Building Out The GUI for our Database App, Delete A Record From Our Database, and Update A Record With SQLite

# Importing the Tkinter library for creating GUI applications
from tkinter import *

# Importing the Image and ImageTk classes from the PIL (Pillow) library for handling images
from PIL import ImageTk, Image

# Importing the sqlite3 library to work with SQLite databases
import sqlite3

# Creating the main window (root widget)
root = Tk()  # Initialize the main application window
root.title("Using Databases With TKinter")  # Setting the title of the window

# Setting the window icon (ensure the path to the icon is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')  # Path to the custom icon

# Setting the initial size of the window
root.geometry('350x500')  # Width x Height in pixels

# Connecting to the SQLite database (or creating it if it doesn't exist)
connection = sqlite3.connect('address_book.db')

# Creating a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the 'addresses' table in the database. After running one time, comment this code.
'''
cursor.execute("""
    CREATE TABLE addresses (
        first_name text,  # Column for the first name
        last_name text,   # Column for the last name
        address text,     # Column for the address
        city text,        # Column for the city
        state text,       # Column for the state
        zipcode integer   # Column for the zipcode
    )
""")
'''

# Create a function to update a record
def update():
    # Declare the editor widgets as global to access them within this function
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Connecting to the SQLite database (or creating it if it doesn't exist)
    connection = sqlite3.connect('address_book.db')  # Establish connection to the database
    cursor = connection.cursor()  # Create a cursor object to execute SQL commands

    # Retrieve the record ID from the delete_box Entry widget
    record_id = delete_box.get()

    # Update the record in the database with new values from the editor widgets
    cursor.execute("""
        UPDATE addresses SET
            first_name = :first,   -- Update first name
            last_name = :last,     -- Update last name
            address = :address,    -- Update address
            city = :city,          -- Update city
            state = :state,        -- Update state
            zipcode = :zipcode     -- Update zipcode
        WHERE oid = :oid""",       # Update the record with the specified ID
                   {
                       'first': f_name_editor.get(),      # Get the updated first name
                       'last': l_name_editor.get(),       # Get the updated last name
                       'address': address_editor.get(),   # Get the updated address
                       'city': city_editor.get(),         # Get the updated city
                       'state': state_editor.get(),       # Get the updated state
                       'zipcode': zipcode_editor.get(),   # Get the updated zipcode
                       'oid': record_id                   # Record ID to identify which record to update
                   }
                   )

    # Commit the changes to the database
    connection.commit()

    # Close the connection to the database
    connection.close()

    # Close the editor window after saving the record
    editor.destroy()


# Create a function to open the editor window for updating records
def edit():
    # Declare editor window and input fields as global variables
    global editor
    global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor

    # Create a new window for editing a record
    editor = Tk()
    editor.title("Update a Record")  # Set the title of the editor window
    editor.iconbitmap(r'C:\Users\musta\tkinter_project')  # Set the window icon
    editor.geometry('350x200')  # Set the dimensions of the editor window

    # Connecting to the SQLite database (or creating it if it doesn't exist)
    connection = sqlite3.connect('address_book.db')  # Establish connection to the database
    cursor = connection.cursor()  # Create a cursor object to execute SQL commands

    # Retrieve the record ID from the delete_box Entry widget
    record_id = delete_box.get()

    # Query the database to retrieve the record with the specified ID
    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cursor.fetchall()  # Fetch all the records (though we expect only one)

    # Create editor text boxes for each field
    f_name_editor = Entry(editor, width=30)  # Create an entry box for the first name
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))  # Position the entry box on the grid
    l_name_editor = Entry(editor, width=30)  # Create an entry box for the last name
    l_name_editor.grid(row=1, column=1)  # Position the entry box on the grid
    address_editor = Entry(editor, width=30)  # Create an entry box for the address
    address_editor.grid(row=2, column=1)  # Position the entry box on the grid
    city_editor = Entry(editor, width=30)  # Create an entry box for the city
    city_editor.grid(row=3, column=1)  # Position the entry box on the grid
    state_editor = Entry(editor, width=30)  # Create an entry box for the state
    state_editor.grid(row=4, column=1)  # Position the entry box on the grid
    zipcode_editor = Entry(editor, width=30)  # Create an entry box for the zipcode
    zipcode_editor.grid(row=5, column=1)  # Position the entry box on the grid

    # Create labels for each field to describe the corresponding text box
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))  # Position the label on the grid
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)  # Position the label on the grid
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)  # Position the label on the grid
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)  # Position the label on the grid
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)  # Position the label on the grid
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)  # Position the label on the grid

    # Populate the text boxes with the current data from the selected record
    for record in records:
        f_name_editor.insert(0, record[0])  # Insert the current first name into the editor
        l_name_editor.insert(0, record[1])  # Insert the current last name into the editor
        address_editor.insert(0, record[2])  # Insert the current address into the editor
        city_editor.insert(0, record[3])  # Insert the current city into the editor
        state_editor.insert(0, record[4])  # Insert the current state into the editor
        zipcode_editor.insert(0, record[5])  # Insert the current zipcode into the editor

    # Create a button to save the updated record
    save_button = Button(editor, text="Save Record", command=update)  # Create a button for saving
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=124)  # Position the button on the grid

# Create a function to delete a record
def delete():
    # Connecting to the SQLite database (or creating it if it doesn't exist)
    connection = sqlite3.connect('address_book.db')
    # Creating a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Deleting the record with the specified ID from the addresses table
    cursor.execute('DELETE FROM addresses WHERE oid=' + delete_box.get())

    # Clearing the delete_box Entry widget after deletion
    delete_box.delete(0, END)

    # Committing the changes to the database
    connection.commit()
    # Closing the connection to the database
    connection.close()


# Create a submit function for database
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
    f_name.delete(0, END)  # Clear the first name text box
    l_name.delete(0, END)  # Clear the last name text box
    address.delete(0, END)  # Clear the address text box
    city.delete(0, END)  # Clear the city text box
    state.delete(0, END)  # Clear the state text box
    zipcode.delete(0, END)  # Clear the zipcode text box

# Create a query function to retrieve and display records from the database
def query():
    # Connecting to the SQLite database (or creating it if it doesn't exist)
    connection = sqlite3.connect('address_book.db')
    # Creating a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Query the database to retrieve all records from the addresses table
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()  # Fetching all the records

    # Prepare the data for display in a formatted string
    print_records = ''
    for record in records:
        print_records += f'{record[0]}, {record[1]}, {record[2]}, {record[3]}, {record[4]}, {record[5]}, \t {record[6]} \n'

    # Create a label widget to display the retrieved records in the GUI
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)  # Positioning the label

    # Committing the changes to the database (even though no changes are made here)
    connection.commit()
    # Closing the connection to the database
    connection.close()

# Create text boxes for user input
f_name = Entry(root, width=30)  # Entry widget for first name
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))  # Positioning the text box
l_name = Entry(root, width=30)  # Entry widget for last name
l_name.grid(row=1, column=1)
address = Entry(root, width=30)  # Entry widget for address
address.grid(row=2, column=1)
city = Entry(root, width=30)  # Entry widget for city
city.grid(row=3, column=1)
state = Entry(root, width=30)  # Entry widget for state
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)  # Entry widget for zipcode
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)  # Entry widget for entering the ID to delete or update
delete_box.grid(row=9, column=1, pady=5)

# Create labels for each text box to indicate what information should be entered
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))
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
delete_box_label = Label(root, text='Select ID')  # Label for the delete/update ID text box
delete_box_label.grid(row=9, column=0, pady=5)

# Create a button to submit the entered data to the database
submit_button = Button(root, text='Add record to database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)  # Positioning the button

# Create a button to query and display records from the database
query_button = Button(root, text='Show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Create a delete button to remove a record from the database
delete_button = Button(root, text='Delete record', command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Create an update button to modify an existing record in the database
edit_button = Button(root, text='Update record', command=edit)
edit_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

# Committing the changes to the database (no changes here, this is redundant)
connection.commit()
# Closing the connection to the database (this is redundant since connection is not used here)
connection.close()

# Running the main event loop to keep the application window open
root.mainloop()

# endregion