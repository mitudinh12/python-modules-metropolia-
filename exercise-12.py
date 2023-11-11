import json
import requests


# 12.1

def main_program_task_1():
    request = "https://api.chucknorris.io/" + "jokes/random"
    response = requests.get(request).json()

    # print(json.dumps(response, indent=2))
    print(response["value"])


# 12.2
def main_program_task_2():
    api_key = "eb68b42775036f9d9b1a56f010b1f00b"
    city_name = input("Give a city name: ")
    coordination_request = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid=" + api_key
    coordination_response = requests.get(coordination_request).json()

    coordination_latitude = coordination_response[0]["lat"]
    coordination_longitude = coordination_response[0]["lon"]

    weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={coordination_latitude}&lon={coordination_longitude}&appid=" + api_key
    weather_response = requests.get(weather_request).json()
    weather_description = weather_response["weather"][0]["description"]
    temperature_kelvin = weather_response["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15

    # print(json.dumps(weather_response, indent=2))
    print(f"Weather condition of {city_name}: {weather_description}")
    print(f"Current temperature: {temperature_kelvin} Kelvin or {temperature_celsius:.2f} Celsius")

