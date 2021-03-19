import random
from tkinter import *
import pandas
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
#make dataframe using pandas
data = pandas.read_csv("data/french_words.csv")
#convert data frame to a dictionary
# french words to learn dictionaries - list of dictionaries
to_learn = data.to_dict(orient="records")
# print(to_learn)


#-----------------------------Generate Random Word Function ___________________#
def next_card():
    #randomly pick data from the to_learn list of dictionaries
    current_card = random.choice(to_learn)
    # print(current_card)
    #value under key French
    # print(current_card["French"])
    # make title the language
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
# ---------------------------- UI --------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 265, image=card_front_img)
card_title =canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

# Buttons

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,command=next_card)
wrong_button.grid(row=2, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=2, column=2)

#call next card for frist time
next_card()

window.mainloop()
