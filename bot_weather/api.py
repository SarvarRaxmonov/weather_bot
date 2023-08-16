import requests
from datetime import datetime, timedelta

url = "https://yahoo-weather5.p.rapidapi.com/weather"



def get_weather(location):
    querystring = {"location": location, "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "0e2c4fbc42msh49019a69acfc209p10198cjsnfe47e01516e1",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()




def next_day():
    today = datetime.now()
    next_day = today + timedelta(days=1)

    next_day_name = next_day.strftime('%A')

    return f"{next_day_name[:3]}"

def dict_format(weather_data):


    weather_dict = {}
    for item in weather_data:
        day = item['day']
        weather_dict[day] = item

    return weather_dict