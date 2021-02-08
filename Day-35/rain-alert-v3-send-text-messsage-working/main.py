

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "#"
account_sid = "#"
auth_token = "3"


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
    # print("Bring an umbrella, it is going to rain today")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_= "#",
        to="#"
    )

    print(message.sid)
