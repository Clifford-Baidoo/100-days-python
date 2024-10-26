from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        #Creating a new turtle and giving it some attributes
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    #Creating two methods that will serve as our up and down methods
    def move_up(self):
        self.forward(MOVE_DISTANCE)  # Move the turtle forward by 10 units

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
    def goto_start(self):
        self.goto(STARTING_POSITION)