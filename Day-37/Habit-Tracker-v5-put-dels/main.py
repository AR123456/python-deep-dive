import requests
# import datetimeclass
from datetime import datetime
USERNAME =""
TOKEN =""
GRAPH = "graph1"
# ###################  account endpoint
pixela_endpoint ="https://pixe.la/v1/users"


# headers dictionary- pass the token in the header
headers = {
    "X-USER-TOKEN": TOKEN
}
#call post method to add a value to the graph
# graph endpoint for posting data to a graph
graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
# today=datetime.now()
# strftime() method 
today=datetime.now().strftime("%Y%m%d")
 
reading_config={
    "date":today,
    "quantity":input("How many pages did you read today\n")
}

response = requests.post(url=graph_endpoint, json=reading_config, headers=headers)

#################### update request- change the quantity to this number
# update_config={
#     "quantity":"5"
# }
# update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today}"
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)

# ################ delete request

# delete_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today}"
# response =requests.delete(url=delete_endpoint, headers=headers)

print(response.text)
