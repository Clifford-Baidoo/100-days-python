from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",15,"normal")

with open("/home/mee_pmeep/Documents/Python_Yu_Project/Day 24/data.txt",mode="r") as high_score:
            contents = int(high_score.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = contents
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            high = str(self.score)
            with open("/home/mee_pmeep/Documents/Python_Yu_Project/Day 24/data.txt",mode="w") as high_score:
                 high_score.write(high)
        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write(f"GAME OVER", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        