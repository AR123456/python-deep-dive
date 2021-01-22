from tkinter import *
from tkinter import messagebox

import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# password_list = []
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
password_letters = [random.choice(letters) for _ in range(nr_letters)]

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

#combine into one list
password_list = password_letters + password_symbols + password_numbers
#then shuffle the list
random.shuffle(password_list)

#changing to use pythons join
# password = ""
# for char in password_list:
#   password += char
password = "".join(password_list)


print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) ==0 or len(password)==0:
        messagebox.showinfo(tile="Opps", message = "Please make sure no fields are empty.")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                              f"Password: {password}\nIs this ok?")
        if is_ok:
            with open("data.txt", mode="a")as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# website
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# method to put the cursor in this box when app launched
website_entry.focus()

# email
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# add a default website to the entry
email_entry.insert(0, "test@test.com")

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, )
# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, )

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
