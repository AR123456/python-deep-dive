import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}\n"))
        if guess < random_number:
            print("Guess too low , try again \n")
        elif guess> random_number:
            print("Guess too high, try again\n")

    print(f"You have guessed the number it was {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L) for correct (C)?? \n").lower()
        if feedback == "h":
            high = guess -1
        if feedback == "l":
            low = guess +1
    print(f"The computer guessed our number which was {guess}\n")

computer_guess(10)
