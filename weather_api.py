# Python script to fetch weather data from an API
import requests

def get_weather(city, latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        response = requests.get(url)
        data = response.json()
        weather = data["current_weather"]
        return f"{city}: {weather['temperature']}°C, Wind: {weather['windspeed']} km/h"
    except:
        return f"Error fetching weather for {city}"

# Fetch weather for London
result = get_weather("London", 51.51, -0.13)
print(result)

# Save to a file
with open("weather_report.txt", "w") as file:
    file.write(result + "\n")
print("Weather saved to weather_report.txt")
