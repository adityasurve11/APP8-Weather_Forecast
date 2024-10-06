import requests

API_KEY = "ddda12c0b7904a6bde1c490350900fed"

def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if Kind == "Tempearture":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]

    return data

if __name__=="main":
    print(get_data(place="Tokyo"))

