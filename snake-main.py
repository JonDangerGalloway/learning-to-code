from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail:
        #trigger game_over



screen.exitonclick()
