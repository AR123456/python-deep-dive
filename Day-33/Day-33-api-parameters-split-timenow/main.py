import requests
from datetime import datetime
## globals for lat and lng
MY_LAT = 51.507351
MY_LNG = -0.127758
TIME_FORMAT = 0

## creating parameters in form of python dictionary
parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":TIME_FORMAT
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

# to get the actual data
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()
# python split to pull ust the time from the unix time
# to get the 24 hr clock time use split
# split by T and then by :
# 2021-01-09T08:02:56+00:00
print(sunrise.split("T"))
print(sunset.split("T"))
# now split on colon
#['2021-01-09', '16:12:55+00:00']
print(sunrise.split("T")[1].split(":"))
print(sunset.split("T")[1].split(":"))
# now getting the first item in the list
#['16', '12', '55+00', '00']
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

# can also write this way
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(time_now.hour)