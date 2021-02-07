# import tkinter
# a better way to import so dont need to use module name over and over
from tkinter import *

#create window
window = Tk()
#title bar
window.title("My first GUI Python program ")
#size
window.minsize(width=500,height=300)

#label
#text and tupel font
my_label = Label(text="I am a label", font=("Arial",24,"bold"))
#.pack() puts on screen and centers it
# my_label.pack()
#can change where it is moved too
# my_label.pack(side="left")
my_label.pack()
# updating the text in the label
# my_label["text"] = "New Text"
#or
my_label.config(text="New Text")
# button
def button_clicked():
    print("I have been clicked")
    new_text=input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#entry or input component
input = Entry(width=10)

input.pack()

input.get()

# Keep window open always at the bottom
window.mainloop()