from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas( height=200,width=200, bg="white", highlightthickness=10, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()
