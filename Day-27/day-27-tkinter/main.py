import tkinter
#create window
window = tkinter.Tk()
#title bar
window.title("My first GUI Python program ")
#size
window.minsize(width=500,height=300)

#label
#text and tupel font
my_label = tkinter.Label(text="I am a label", font=("Arial",24,"bold"))
#.pack() puts on screen and centers it
# my_label.pack()
#can change where it is moved too
my_label.pack(side="bottom")


# Keep window open always at the bottom
window.mainloop()