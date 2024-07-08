from turtle import Turtle, Screen

iris = Turtle()
screen = Screen()

def moveforward():
    iris.forward(10)

def movebackward():
    iris.backward(10)

def clockmove():
    iris.right(5)

def countermove():
    iris.left(5)

def cleardesk():
    iris.home()
    iris.clear()



screen.listen()
screen.onkey(key = "w",fun = moveforward)
screen.onkey(key = "s",fun = movebackward)
screen.onkey(key = "a",fun = countermove)
screen.onkey(key = "d",fun = clockmove)
screen.onkey(key = "c",fun = cleardesk)





























screen.exitonclick()
