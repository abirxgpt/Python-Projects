import pandas
import turtle
from turtle import Screen
from name_display import NameDisplay

states_data = pandas.read_csv("28_states.csv")
state_list = states_data["state"].to_list()
x_state_list = states_data["x"].to_list()
y_state_list = states_data["y"].to_list()

window = Screen()
window.setup(width=871, height=1017)
window.title("India States Guess Game")
window.bgcolor("black")
img_path = "india_blank_map.gif"
window.addshape(img_path)


turtle.shape(img_path)

state_guessed = 0
keep_guessing = True
while keep_guessing:
    user_answer = window.textinput(title=f"Guess the State: {state_guessed}/29", prompt="What's Another State Name?").title()

    if user_answer in state_list:
        state_guessed += 1
        index_number = state_list.index(user_answer)
        x = NameDisplay()
        x.show_name(x_state_list[index_number], y_state_list[index_number], user_answer)
        state_list.remove(user_answer)
        x_state_list.remove(x_state_list[index_number])
        y_state_list.remove(y_state_list[index_number])

    if state_guessed == 29:
        x = NameDisplay()
        x.congratulations()
        keep_guessing = False

    if user_answer == "Exit":
        x = NameDisplay()
        keep_guessing = False
        x.onexit(state_guessed)

window.exitonclick()
