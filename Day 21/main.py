from turtle import Screen
from snake_body import SnakeBody
import time
from food import Food
from scoreboard import Scoreboard

window = Screen()
window.setup(width=600, height=600)
window.title("Snake Game")
window.bgcolor("black")
window.tracer(0)

snake = SnakeBody()
food = Food()
score_monitor = Scoreboard()


window.listen()
window.onkey(SnakeBody.forward, "Up")
window.onkey(SnakeBody.backward, "Down")
window.onkey(SnakeBody.righty, "Right")
window.onkey(SnakeBody.lefty, "Left")

# Variables
is_on = True


while is_on:
    window.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.reset()
        food = Food()
        score_monitor.increase()
        snake.adding()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score_monitor.reset_game()
        snake.reset_snake()

    for segment in snake.segment[1:-1]:
        if snake.head.distance(segment) < 10:
            score_monitor.reset_game()
            snake.reset_snake()

window.exitonclick()
