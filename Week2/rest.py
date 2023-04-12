from datetime import datetime, timedelta
import requests
import json

def is_raining(lat, lon, api_key):
    """
    Reads the api_data and checks to see if the weather is currently raining
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url)
    data = json.loads(response.text)

    if data["weather"][0]["main"] == "Rain":
        print("It is raining in Portland, OR")
    else:
        print("It is not raining in Portland, OR")


def forecast(lat, lon, cnt, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    next_class_day = datetime.now() + timedelta(days=cnt)
    target_date = next_class_day.strftime("%Y-%m-%d")

    parsed_data = [
        item for item in data["list"] if item["dt_txt"][:-9] == str(target_date)
    ]
    for temp in parsed_data:
        if temp["weather"][0]["main"] == "Rain":
            print("It is raining in Portland, OR on our next class period")
            return

    print("It is not raining in Portland, OR on our next class period")


def main():
    with open("./auth.json") as keys:
        api_key = json.load(keys)["api_key"]

    lat = "45.5152"
    lon = "-122.6784"

    is_raining(lat, lon, api_key)

    curr_day = datetime.now().weekday()

    if curr_day == 0:
        forecast(lat, lon, 2, api_key)
    elif curr_day < 2:
        forecast(lat, lon, 1, api_key)
    elif curr_day == 2:
        forecast(lat, lon, 5, api_key)
    elif curr_day > 2:
        forecast(lat, lon, 5 - curr_day, api_key)


main()
