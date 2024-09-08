import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/3.0/weather"

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json
        weather_info = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
        return weather_info
    else:
        return {"error": "Cidade não encontrada na API"}