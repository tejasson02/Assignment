import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
        else:
            print(f"Failed to retrieve weather information. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    api_key = "88c2ec985c3c68d144fbd1d044147a4c"
    city_name = input("Enter city name: ")

    get_weather(api_key, city_name)


if __name__ == "__main__":
    main()
