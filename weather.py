import requests

API_KEY = "74a0157a5233ed2016c28add57d9aec2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'] 
    temperature = data["main"]["temp"]

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
    
else:
    print("An error occurred.")
