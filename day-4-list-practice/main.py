
# list of states ordered by when they joined 
# union 
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
# prints the state in that position in the list 
# like arrays lists start at 0 , 
# think of this as an offset or shift 
print(states_of_america[5])
# can also use a negative index to start counting from end of list -1 gets end of list 
print(states_of_america[-1])
# can change or alter items in the list too
states_of_america[1] = "Pencilvanya"
print(states_of_america)
# can add itmes to the list
states_of_america.append("Anneland")
print(states_of_america)
states_of_america.extend(["Anneland","Samland"])
print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

