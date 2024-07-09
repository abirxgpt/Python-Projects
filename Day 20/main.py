from turtle import Screen
from snake_body import SnakeBody
import time

window = Screen()
window.setup(width=600, height=600)
window.title("Snake Game")
window.bgcolor("black")
window.tracer(0)

snake = SnakeBody()


window.listen()
window.onkey(SnakeBody.forward, "Up")
window.onkey(SnakeBody.backward, "Down")
window.onkey(SnakeBody.righty, "Right")
window.onkey(SnakeBody.lefty, "Left")

is_on = True
while is_on:
    window.update()
    time.sleep(0.1)

    snake.move()


window.exitonclick()
