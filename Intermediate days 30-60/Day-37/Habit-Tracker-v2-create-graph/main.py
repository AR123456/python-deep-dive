import requests
USERNAME =" "
TOKEN =" "
# ################### create account endpoint
pixela_endpoint ="https://pixe.la/v1/users"
user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response =requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# ################ create graph definition post request
graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
#  graph config
graph_config ={
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type":"float",
    "color":"ajisai"
}
# headers dictionary- pass the token in the header
headers = {
    "X-USER-TOKEN": TOKEN
}
# call post method
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)