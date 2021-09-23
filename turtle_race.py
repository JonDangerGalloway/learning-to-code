import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = turtle.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_spot = -70
turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_spot)
    y_spot += 30
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = (turtle.pencolor())
            if winning_color == user_bet:
                print(f"You've Won. The {winning_color} is the winner!")
            else:
                print(f"You've lost. The {winning_color} is the winner!")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
