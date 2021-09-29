from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.increase_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)
        self.score += 1


