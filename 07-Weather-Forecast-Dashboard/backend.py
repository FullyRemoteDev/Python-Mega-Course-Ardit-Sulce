import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('APP7_API_KEY')


def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    filtered_data = weather_data['list']
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]

    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    elif kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data


if __name__ == '__main__':
    print(get_data(place='Tokyo', forecast_days=3, kind='Temperature'))
