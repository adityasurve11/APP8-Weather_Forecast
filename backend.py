import requests

API_KEY = "ddda12c0b7904a6bde1c490350900fed"

def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return data

if __name__=="main"
    get_data()

