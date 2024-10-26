from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_level(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("Courier",15,"bold"))