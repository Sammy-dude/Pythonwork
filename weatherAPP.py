import json
import tkinter as tk
from tkinter import ttk
import requests

# Replace this with your own OpenWeatherMap API key
API_KEY = '2c710da31ca7d6a110c6dadee173acc0'


# Function to get weather information based on city name
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    # print(json.dumps(response, indent=4))
    print(json.dumps(response.json(), indent=4))
    if response.status_code == 200:
        weather_data = response.json()
        weather = {
            'City': weather_data['name'],
            'Temperature': weather_data['main']['temp'],
            'Description': weather_data['weather'][0]['description'],
            'Humidity': weather_data['main']['humidity'],
            'Wind Speed': weather_data['wind']['speed']
        }
        return weather

    else:
        return None


# Function to display the weather details in the GUI
def show_weather():
    city = city_combobox.get()
    weather = get_weather(city)

    if weather:
        result_label.config(text=f"City: {weather['City']}\n"
                                 f"Temperature: {weather['Temperature']}°C\n"
                                 f"Description: {weather['Description']}\n"
                                 f"Humidity: {weather['Humidity']}%\n"
                                 f"Wind Speed: {weather['Wind Speed']} m/s")
    else:
        result_label.config(text="City not found or error in API call")


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

# Button to trigger weather fetch
get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack(pady=10)

# Label to display the weather result
result_label = tk.Label(app, text="", font=("Helvetica", 10), justify=tk.LEFT)
result_label.pack(pady=20)

# Run the Tkinter main loop
app.mainloop()
