import random
from tkinter import *
from random import *
import pandas
# ---------------------------- IMPORT DATA ------------------------------- #
try:
    lang_data = pandas.read_csv("Words_To_Learn.csv")
except:
    lang_data = pandas.read_csv("Italian.csv")
finally:
    italian_english = lang_data.to_dict(orient="records")

# ---------------------------- CONSTANTS ------------------------------- #
SUB_HEAD_TEXT = ('Ariel', 40, 'italic')
HEAD_TEXT = ('Ariel', 60, 'bold')
BACKGROUND_COLOR = "#B1DDC6"
Current_Card = {}

# ---------------------------- Next Card ------------------------------- #
def next_card():
    global Current_Card, timer
    Current_Card = choice(italian_english)
    italian_word = Current_Card["Italian"]
    images.itemconfig(canvas_image, image=card_front)
    images.itemconfig(canvas_title, text="Italian", fill="black")
    images.itemconfig(canvas_word, text=italian_word, fill="black")
    timer = window_screen.after(3000, flip_card)


# ---------------------------- TICK MARK ------------------------------- #
def is_known():
    italian_english.remove(Current_Card)
    new_data = pandas.DataFrame(italian_english)
    new_data.to_csv("./Words_To_Learn.csv", index=False)
    next_card()


# ---------------------------- Flip Card ------------------------------- #
def flip_card():
    images.itemconfig(canvas_image, image=card_back)
    english_word = Current_Card["English"]
    images.itemconfig(canvas_title, text="English", fill="white")
    images.itemconfig(canvas_word, text=english_word, fill="white")


# ---------------------------- UI SETUP ------------------------------- #
# Main Screen
window_screen = Tk()
window_screen.title("Flearn")
window_screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window_screen.after(3000, flip_card)

# Image Loader
card_back = PhotoImage(file="card_back.png")
card_front = PhotoImage(file="card_front.png")
tick = PhotoImage(file="tick.png")
mark = PhotoImage(file="mark.png")

# Canvas
images = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = images.create_image(400,263, image=card_front)
canvas_title = images.create_text(400,150,text="Italian",font=SUB_HEAD_TEXT)
canvas_word = images.create_text(400,263,text="di",font=HEAD_TEXT)
images.grid(column=0, row=0, columnspan=2)

# Buttons
tick_button = Button(image=tick, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
tick_button.grid(column=0, row=1)
mark_button = Button(image=mark, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
mark_button.grid(column=1, row=1)

next_card()

window_screen.mainloop()
