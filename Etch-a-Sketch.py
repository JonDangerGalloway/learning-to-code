import turtle
from turtle import Turtle, Screen


#    W = Forwards
#    S - Backwrds
#    A - Left
#    D- Right
#    C - Clear drawing and put turtle back in center
#

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)

def clear():
    tim.hideturtle()
    tim.clear()
    tim.penup()
    tim.home()
    tim.showturtle()
    tim.pendown()


screen.listen()
turtle.onkey(key="w", fun=move_forwards)
turtle.onkey(key="s", fun=move_backwards)
turtle.onkey(key="a", fun=turn_left)
turtle.onkey(key="d", fun=turn_right)
turtle.onkey(key="c", fun=clear)


screen.exitonclick()