from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwords.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site = website.get()
    mailid = mail.get()
    passwd = passwords.get()

    if len(site) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Error", message="Please Make sure no Fields are Left Empty")
    else:
        move_ahead = messagebox.askokcancel(title=site, message=f"These are your Credentials:\nMail/Username: {mailid}\nPassword: {passwd}\nIs it okay to Save?")
        if move_ahead:
            with open("data.txt", mode="a") as data:
                data.write(f"{site} | {mailid} | {passwd}\n")
            website.delete(0, END)
            passwords.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Main Screen
window_screen = Tk()
window_screen.title("Password Manager")
window_screen.config(padx=20, pady=20)


# Image Loader
pass_img = PhotoImage(file="password_imgdas.png")

# Canvas
images = Canvas(width=300, height=300)
images.create_image(170, 150, image=pass_img)
images.grid(column=1, row=0)

# Buttons
Generate_button = Button(text="Generate Password", command=generate_password)
Generate_button.grid(column=2, row=3, sticky="EW")
Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# Entries
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2, sticky="EW")
website.focus()
mail = Entry(width=35)
mail.grid(column=1, row=2, columnspan=2, sticky="EW")
mail.insert(0, "abir.guptaaa@gmail.com")
passwords = Entry(width=21)
passwords.grid(column=1, row=3, sticky="EW")

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

window_screen.mainloop()
