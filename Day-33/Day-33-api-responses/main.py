import requests
# requests.get is the syntax to use for making the get request
# set it equal to the var response
response =requests.get(url="http://api.open-notify.org/iss-now.json")
# this will print the response code not the JSON object
# print(response)
# # print just the response code
# print(response.status_code)
# use the requests module
response.raise_for_status()
# to get the actual data
data = response.json()
# can drill down into data as would a python dictionary - here passing in key
position = response.json()["iss_position"]
# here drilling down further
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(f"{data}\n{position}\n{longitude}\n{latitude}\n")
# making a tupple
iss_position = (latitude,longitude)
print (iss_position)
