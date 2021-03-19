import requests
# requests.get is the syntax to use for making the get request
# set it equal to the var response
response =requests.get(url="http://api.open-notify.org/iss-now.json")
# this will print the response code not the JSON object
print(response)