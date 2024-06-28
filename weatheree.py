import requests
from tkinter import Tk, Label, Entry, Button, Frame, messagebox

# Function to get weather data
def get_weather():
    city = city_entry.get()
    
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    # Geocoding to get latitude and longitude for the city
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geocoding_response = requests.get(geocoding_url).json()
    
    if geocoding_response['results']:
        lat = geocoding_response['results'][0]['latitude']
        lon = geocoding_response['results'][0]['longitude']
        
        # Get weather data using latitude and longitude
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()
        
        temp = weather_response['current_weather']['temperature']
        weather_code = weather_response['current_weather']['weathercode']
        
        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Drizzle: Light",
            53: "Drizzle: Moderate",
            55: "Drizzle: Dense intensity",
            56: "Freezing Drizzle: Light",
            57: "Freezing Drizzle: Dense intensity",
            61: "Rain: Slight",
            63: "Rain: Moderate",
            65: "Rain: Heavy intensity",
            66: "Freezing Rain: Light",
            67: "Freezing Rain: Heavy intensity",
            71: "Snow fall: Slight",
            73: "Snow fall: Moderate",
            75: "Snow fall: Heavy intensity",
            77: "Snow grains",
            80: "Rain showers: Slight",
            81: "Rain showers: Moderate",
            82: "Rain showers: Violent",
            85: "Snow showers slight",
            86: "Snow showers heavy",
            95: "Thunderstorm: Slight or moderate",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail"
        }
        
        weather_desc = weather_codes.get(weather_code, "Unknown weather code")
        
        weather_label.config(text=f"Temperature: {temp}°C\nDescription: {weather_desc}")
    else:
        weather_label.config(text="City not found. Please enter a valid city name.")

# Setting up the GUI
root = Tk()
root.title("Simple Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Main frame
frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

city_label = Label(frame, text="Enter city name:", font=("Arial", 14))
city_label.pack(pady=10)

city_entry = Entry(frame, font=("Arial", 14), width=25)
city_entry.pack(pady=5)

get_weather_button = Button(frame, text="Get Weather", font=("Arial", 14), command=get_weather, bg="#4CAF50", fg="white")
get_weather_button.pack(pady=20)

weather_label = Label(frame, text="", font=("Arial", 14))
weather_label.pack(pady=10)

root.mainloop()
