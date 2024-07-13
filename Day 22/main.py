from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


window = Screen()
window.setup(width=800, height=600)
window.title("Pong Game")
window.bgcolor("black")
window.tracer(0)

l_paddle = Paddle((-375, 0))
r_paddle = Paddle((375, 0))
ball = Ball()
score = Scoreboard()

window.listen()
window.onkey(r_paddle.up, "Up")
window.onkey(r_paddle.down, "Down")
window.onkey(l_paddle.up, "w")
window.onkey(l_paddle.down, "s")


Game_on = True

while Game_on:
    window.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 365:
        ball.paddle_bounce()

    if l_paddle.distance(ball) < 50 and ball.xcor() < -365:
        ball.paddle_bounce()

    if ball.xcor() > 395:
        ball.reset_pos()
        score.increase_l()
        ball.speed_reset()

    if ball.xcor() < -395:
        ball.reset_pos()
        score.increase_r()
        ball.speed_reset()

window.exitonclick()
