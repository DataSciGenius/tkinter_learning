# Link 1: https://youtu.be/vJCjDevYDt8?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 2: https://youtu.be/ARQH_3_Erao?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# Link 3: https://youtu.be/Lcb6PTjnTOo?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# region Building a Weather App, Change Colors In our Weather App & Add Zipcode Lookup Form

# Importing the Tkinter library for creating GUI applications
from tkinter import *

# Importing the Image and ImageTk classes from the PIL (Pillow) library for handling images
from PIL import ImageTk, Image

# Importing the requests library to make HTTP requests, and the json library to handle JSON data
import requests
import json

# Creating the main window (root widget) for the application
root = Tk()

# Setting the title of the main window to "Building a Weather App"
root.title("Building a Weather App")

# Setting the icon of the main window (ensure the path to the icon file is correct)
root.iconbitmap(r'C:\Users\musta\tkinter_project')

# Setting the initial size of the main window to 700 pixels wide and 100 pixels tall
root.geometry('700x100')

# API Source
# https://docs.airnowapi.org/
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7E4F2C4C-2292-4D81-BDC3-684BBF894FA8
# [{"DateObserved":"2024-08-12","HourObserved":13,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"O3","AQI":42,"Category":{"Number":1,"Name":"Good"}},{"DateObserved":"2024-08-12","HourObserved":13,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM2.5","AQI":36,"Category":{"Number":1,"Name":"Good"}},{"DateObserved":"2024-08-12","HourObserved":13,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM10","AQI":37,"Category":{"Number":1,"Name":"Good"}}]

# las_vegas_zipcode = 89199 - Green
# Coeur D Alene, Idaho = 83814 - Yellow

# Create a zipcode lookup function
def zip_lookup():
    # This function fetches air quality data based on the provided ZIP code and updates the GUI.

    try:
        # Make an API request to retrieve air quality data for the provided ZIP code
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="
            + zip_code.get() + "&distance=5&API_KEY=7E4F2C4C-2292-4D81-BDC3-684BBF894FA8")

        # Parse the JSON data received from the API
        api = json.loads(api_request.content)

        # Extracting relevant information from the API response
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        # Determine background color based on the air quality category
        if category == 'Good':
            whether_color = '#0C0'  # Green
        elif category == 'Moderate':
            whether_color = '#FFFF00'  # Yellow
        elif category == 'Unhealthy for Sensitive Groups':
            whether_color = '#ff9900'  # Orange
        elif category == 'Unhealthy':
            whether_color = '#FF0000'  # Red
        elif category == 'Very Unhealthy':
            whether_color = '#990066'  # Purple
        elif category == 'Hazardous':
            whether_color = '#660000'  # Maroon

        # Update the background color of the root window based on the air quality
        root.configure(background=whether_color)

        # Display the air quality information in a label
        my_label = Label(root, text=f'Air Quality of {city}: {quality} and {category}', font=('Helvetica', 20), background=whether_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        # Handle errors (e.g., network issues, invalid ZIP code)
        api = 'Error...'

# Creating an Entry widget for user input to enter the ZIP code
zip_code = Entry(root)
zip_code.grid(row=0, column=0, stick=W + E + N + S)

# Creating a Button widget that triggers the zip_lookup function when clicked
zip_button = Button(root, text='Lookup Zipcode', command=zip_lookup)
zip_button.grid(row=0, column=1, stick=W + E + N + S)

# Running the main event loop to keep the application window open
root.mainloop()

# endregion