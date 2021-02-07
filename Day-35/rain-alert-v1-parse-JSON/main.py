import requests



api_key = "b2c2945f3a35f0db5d92a82713e51c09"

# my_lat = 39.729431
# my_lon = -104.831917

my_lat = 43.907360
my_lon = 39.332800

url ="https://api.openweathermap.org/data/2.5/onecall"

parameters ={
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response=requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:11]
will_rain = False

# loop weather slice
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain == True:
    print("Bring an umbrella")



# print(weather_data["hourly"][0]["weather"][0]["id"])
