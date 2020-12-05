# import art and game data
from art import logo,vs
from game_data import data
import random
from replit import clear
# Generate a random selection from the game data.
def get_random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"
# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  # game variables
  score =0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()
  
  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()
    if account_a == account_b:
      account_b = get_random_account()
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? type'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score +=1
      print(f" You are right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry that is not correct. Final score:{score}")

game()
