#imports 
from random import randint
from art import logo

#Globals 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Functions 
#Function to check user's guess against actual answer.
# passing in turns so that it can be returned to avoid altering global scope in this function - turns is comeing from the set difficulty function 
def check_answer(guess,answer,turns):
  # this doc string will show up when coder overs for the function when it gets called 
  """checks answer agains guess and returns number of turns remaining"""
  if guess > answer:
    print("That was too high.\n ")
    return turns -1
  elif guess < answer:
    print("That was too low\n  ")
    return turns -1
  else:
    print("You got it ! ")
#Make function to set difficulty.
def set_difficulty():
  level = input("Choose difficulty. Type 'easy' or 'hard': \n")
  if level =="easy":
    # need to return as output from the funciton to use later
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game ! \n I am thiking of a number between 1 and 100\n")
  answer = randint(1,100)
  print(f"For testing the number is {answer}")

  turns = set_difficulty()
  print(f"You have {turns} attempts remaining")

  #Repeat the guessing functionality if they get it wrong.
  guess =0
  while guess != answer:
    #Let the user guess a number.
    guess = int(input("Make a guess: "))
  #pass turns in too setting it to turns will update to local variable every time answer is checked 
    turns = check_answer(guess,answer,turns)
    print(f"You have {turns} attempts remaining")
    if turns == 0:
      print("No more guesses ")
      return
 
   


#Track the number of turns and reduce by 1 if they get it wrong. 
#calling this in the global scope 
game()
 

 

 


 


 
