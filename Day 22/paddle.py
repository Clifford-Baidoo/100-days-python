from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        

    def move_up(self):
        self.new_y = self.ycor() + 10
        self.goto(self.xcor(),self.new_y)

    def move_down(self):
        self.new_y = self.ycor() - 10
        self.goto(self.xcor(),self.new_y)

