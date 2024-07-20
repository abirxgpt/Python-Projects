from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#88D66C"
YELLOW = "#FEFBD8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_clock = None


# ---------------------------- JUMP TOP ------------------------------- #
def raise_above_all():
    window_screen.attributes('-topmost', 1)
    window_screen.attributes('-topmost', 0)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_countdown():
    window_screen.after_cancel(timer_clock)
    global reps
    reps = 0
    images.itemconfig(timer, text="00:00")
    title.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():

    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        raise_above_all()
        title.config(text="Timer", fg=GREEN)
        countdown(work_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        title.config(text="Break", fg=PINK)
        raise_above_all()
        countdown(short_break_sec)
    elif reps == 8:
        title.config(text="Break", fg=RED)
        raise_above_all()
        countdown(long_break_sec)
    elif reps > 8:
        raise_above_all()
        reset_countdown()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    images.itemconfig(timer, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer_clock
        timer_clock = window_screen.after(1000, countdown, count-1)
    else:
        timer_start()
    mark = ""
    for _ in range(math.floor(reps/2)):
        mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
# Main Screen
window_screen = Tk()
window_screen.title("Pomodoro Timer")
window_screen.config(padx=100, pady=50, bg=YELLOW)


# Image Loader
tom_image = PhotoImage(file="tomato.png")

# Canvas
images = Canvas(width=360, height=360, bg=YELLOW, highlightbackground=YELLOW)
images.create_image(180, 180, image=tom_image)
timer = images.create_text(180, 200, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
images.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=timer_start)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_countdown)
reset_button.grid(column=3, row=3)

# Labels
title = Label(text="Timer", fg=GREEN, font=("times new roman", 50, "bold"), bg=YELLOW)
title.grid(column=1, row=0)
check_mark = Label(text="", fg=GREEN, font=("arial", 20, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=4)

window_screen.mainloop()
