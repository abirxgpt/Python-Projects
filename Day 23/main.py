from turtle import Screen
from Turtle import Player
from scoreboard import LevelBoard
from car_manager import CarManager
import time

window = Screen()
window.setup(600, 600)
window.bgcolor("white")
window.tracer(0)

player_turtle = Player()
level = LevelBoard()
car = CarManager()

window.listen()
window.onkey(player_turtle.ahead, "Up")
window.onkey(player_turtle.behind, "Down")

def game_play():
    car.reset_game()
    level.reset_score()
    player_turtle.next_level()

    is_running = True
    while is_running:
        time.sleep(0.1)
        window.update()

        car.create_car()
        car.move_car()

        for cars in car.multiple_cars:
            if cars.distance(player_turtle) < 20:
                level.game_over()
                is_running = False

        if player_turtle.ycor() > 295:
            level.increase()
            player_turtle.next_level()
            car.speed_increase()


window.onkey(game_play, "r")

is_running = True
while is_running:
    time.sleep(0.1)
    window.update()

    car.create_car()
    car.move_car()

    for cars in car.multiple_cars:
        if cars.distance(player_turtle) < 20:
            level.game_over()
            is_running = False

    if player_turtle.ycor() > 295:
        level.increase()
        player_turtle.next_level()
        car.speed_increase()

window.exitonclick()
