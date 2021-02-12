import requests
USERNAME =""
TOKEN =""
GRAPH = "graph1"
# ################### create account endpoint
pixela_endpoint ="https://pixe.la/v1/users"
user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# ################ create graph definition post request
# graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
# #  graph config
# graph_config ={
#     "id": "graph1",
#     "name": "Reading Graph",
#     "unit": "Pages",
#     "type":"float",
#     "color":"ajisai"
# }
# headers dictionary- pass the token in the header
headers = {
    "X-USER-TOKEN": TOKEN
}
# call post method to create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#call post method to add a value to the graph
# graph endpoint for posting data to a graph
graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
reading_config={
    "date":"20210123",
    "quantity":"4"
}
response = requests.post(url=graph_endpoint, json=reading_config, headers=headers)