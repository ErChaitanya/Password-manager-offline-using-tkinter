import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import random
import pyperclip # this library is help to use for just simply pasting the generating password to anywhere without copying it as it copy by itself.


# Constant
from sqlalchemy import column

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
# import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # the two below comments line just after code indicates the alternative in the format of list comprehensions.
    # password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # password_symbols = [random.choice(letters) for _ in range(random.randint(2, 4))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # password_number = [random.choice(letters) for _ in range(random.randint(2, 4))]
    password_number = [choice(letters) for _ in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_number + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    # ☝  alternative of above code is commented out as below.️
    # password = "" # Empty string
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0, password) # This line is help to insert the generated password on that respective entry box.
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPs", message="Please make sure you haven't left any field empty.")

    else:

        # work for the pop-up window
        #     messagebox.showinfo(title="Title", message="Message")
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the you have been entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save:")

        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# Upto this above save function is worked fine to save the data inside the entry box
# But the below code is use for clearing the entries after every old one is done.
#
#     with open("data.txt", "a") as data_file:
#         data_file.write(f"{website} | {email} | {password}\n")
#
#         website_entry.delete(0, END)
#         password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=200, height=200)
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=44)
website_entry.grid(column=1, row=1, columnspan=3)
website_entry.focus()  # this helps to start curser to website_entry box
email_entry = Entry(width=44)
email_entry.grid(column=1, row=2, columnspan=3)
email_entry.insert(0, "chaitanya@gmail.com")  # this line is use to insert / readily filled email in email entry box
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
# , font=(FONT_NAME, 10)
# , columnspan=2
