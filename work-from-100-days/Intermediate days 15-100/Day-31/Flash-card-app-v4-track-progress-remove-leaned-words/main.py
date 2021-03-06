import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card ={}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#-----------------------------Generate Random Word Function ___________________#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer= window.after(3000, func=flip_card)
# -------------------------Flip Card Function -----------------------------------#
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)
#---------------------------Function to remove known word from list _____________#
def is_known():
    #remove this dictionary from the to learn list
    to_learn.remove(current_card)
    #save the to learn list to a new csv
    data = pandas.DataFrame(to_learn)
    #telling pandas not to repeatedly add index column to csv
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI --------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
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
# user knows this word so remove it from the list to learn
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=2, column=2)

#call next card for frist time
next_card()

window.mainloop()
