from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
#-----------------------------Generate Random Word Function ___________________#
def rand_word():
    print("you clicked on a button ")
    # get the data from the file in a format that is usable list or dictionary ?
    # loop over the items in the French column and pick a random word store in word var
    # switch out the  text that is now Word with that var
#HINT:

# 1. You'll need to use pandas to access the CSV file and generate a data frame.
# To get all the words/translation rows out as a list of dictionaries e.g.
# [{french_word: english_word}, {french_word2: english_word2}, {french_word3: english_word3}]
#
# You could use:
#
# DataFrame.to_dict(orient="records")
#
# Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
# ---------------------------- UI --------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 265, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

# Buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,command=rand_word)
wrong_button.grid(row=2, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=rand_word)
right_button.grid(row=2, column=2)

window.mainloop()
