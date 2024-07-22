from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
import popup

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
    pass_data = {site: {
        "email": mailid,
        "password": passwd
    }}

    if len(site) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Error", message="Please Make sure no Fields are Left Empty")
    else:
        try:
            with open("data.json", mode="r") as data:
                # reading previous file
                prev_file = json.load(data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                json.dump(obj=pass_data, fp=data, indent=4)
        else:
            # Updating previous file as new file
            prev_file.update(pass_data)
            with open("data.json", mode="w") as data:
                # writing new file to json file
                json.dump(obj=prev_file, fp=data, indent=4)
        finally:
            website.delete(0, END)
            passwords.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# To find the password when search button is pressed
def find_password():
    site = website.get()
    try:
        with open("data.json", mode="r") as data:
            prev_file = json.load(data)
    except FileNotFoundError:
        popup.Popup(title="Error", message=f"Please Input and Add some Details first!!")
    else:
        if site in prev_file:
            popup.Popup(title=site, message=f"Here are your credentials of {site}\nMail/Username: {prev_file[site]['email']}\nPassword: {prev_file[site]['password']}")
        else:
            popup.Popup(title="Error", message=f"No details for the Website: {site} Exists!")


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
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

# Entries
website = Entry(width=21)
website.grid(column=1, row=1, sticky="EW")
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
