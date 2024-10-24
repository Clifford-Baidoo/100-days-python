from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        

    def create_snake(self):
        for i in STARTING_POSITIONS:
           self.add_square(i)

    def add_square(self,i):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.squares.append(tim)

    def extend_square(self):
        self.add_square(self.squares[-1].position())

    def move(self):
        for seg_num in range(len(self.squares) - 1,0,-1):#Create a for statement that uses the start stop and step which makes the for loop start from the first square instead of the last one
            new_x = self.squares[seg_num - 1].xcor() #sets a new x coordinate
            new_y = self.squares[seg_num - 1].ycor() #sets a new y coordinate
            self.squares[seg_num].goto(new_x,new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
