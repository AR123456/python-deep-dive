travel_log = [
{
  "country": "France",
  "visits": 12,
    # this is a list nested inside of a dictionary 
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  # this is a list nested inside of a dictionary 
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,visits,cities):
  # each entry in travel_log list is a dictionary 
  # in order to add to the travel_log list create a new 
  # empty dictionary with all of the 
  # pieces of data in it
  # for each key in the dictionary 
  new_country ={}
  # key value added 
  # ["key"]=value
  new_country["country"]=country
  new_country["visits"] =visits 
  new_country["cities"] =cities
# append a list vs add to a dictionary
  travel_log.append(new_country)
 #🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



