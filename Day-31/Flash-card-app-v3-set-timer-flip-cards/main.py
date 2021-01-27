import random
from tkinter import *
import pandas
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
# set current_card dictionary to a global , start with empty
current_card ={}

#-----------------------------Generate Random Word Function ___________________#
def next_card():
    #grab the global var current_card and flip timer
    global current_card, flip_timer
    #cancel the old flip timer if user clicked next before it ran out
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background,image=card_front_img)
    # reset / set new flip_timer for this card
    flip_timer= window.after(3000, func=flip_card)
# -------------------------Flip Card Function -----------------------------------#
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    #change to back_card image
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- UI --------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# set timer, set to var make it a global
flip_timer =window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 265, image=card_front_img)
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
