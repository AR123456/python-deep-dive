# import art and game data
from art import logo,vs
from game_data import data
import random
from replit import clear

# make a function that loops through the game data list and randomly finds a dictionary item in the list.  
def get_A():
  
  compare_1 = (random.choice(data))
  name1 = (compare_1.get("name"))
  followers1 = (compare_1.get("follower_count"))
  description1= (compare_1.get("description"))
  country1 = (compare_1.get("country"))
  # print(f"{name1},{followers1},{description1},from {country1}")

def get_B():
  compare_2 = (random.choice(data))
  return:
    name2 = (compare_2.get("name"))
    followers2 = (compare_2.get("follower_count"))
    description2= (compare_2.get("description"))
    country2 = (compare_2.get("country"))
  # print(f"{name2},{followers2},{description2},from {country2}")


#For the fond list, show the name, description, from country , store the values in followers 
# make this compare_1 
# use the function to make compare_2
# feed compare_1 and compare_2 into compare followers in, the compare with the most wins 
# if correct increment score and the correct answer becomes the new "A"
# if ever wrong print("Sorry, that is wrong.\n Final score : {score}")


print(logo)
get_A()
get_B()
 
compare = input(f"Compare A: {name1}\n {vs}\n Against B:{name2} Who has more followers?\n Type'A' or 'B' : \n")