import json
import tkinter as tk
from tkinter import ttk
import requests

# Replace this with your own OpenWeatherMap API key
API_KEY = '2c710da31ca7d6a110c6dadee173acc0'


# Function to fetch and display weather information
def show_weather():
    city = city_combobox.get()

    # API call to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        print(json.dumps(weather_data, indent=4))
        # Extract required fields from the JSON response
        # city_name = weather_data['name']
        # temperature = weather_data['main']['temp']
        # description = weather_data['weather'][0]['description']
        # humidity = weather_data['main']['humidity']
        # wind_speed = weather_data['wind']['speed']

        # Update the result label with the weather information
        result_label.config(text=f"City: {weather_data['name']}\n"
                                 f"Statue Code: {weather_data['cod']}\n"
                                 f"Temperature: {weather_data['main']['temp']}°C\n"
                                 f"Description: {weather_data['weather'][0]['description']}\n"
                                 f"Humidity: {weather_data['main']['humidity']}%\n"
                                 f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        result_label.config(text="City not found or error in API call")
# def clear_combobox(event):
#     city_combobox.set('')

# Create the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

# Label for the city dropdown
city_label = tk.Label(app, text="Enter City or Select from List:", font=("Helvetica", 12))
city_label.pack(pady=10)

# List of pre-populated cities
cities = ['New York', 'Los Angeles', 'London', 'Paris', 'Tokyo']

# Create a combobox (dropdown) that allows typing
city_combobox = ttk.Combobox(app, values=cities)
city_combobox.pack(pady=10)
city_combobox.set('Type or Select City')
city_combobox.bind("<Button-1>", lambda event: city_combobox.set(''))

# Button to trigger weather fetch
get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)

# Label to display the weather result
result_label = tk.Label(app, text="", font=("Helvetica", 10), justify=tk.LEFT)
result_label.pack(pady=20)

# Run the Tkinter main loop
app.mainloop()
