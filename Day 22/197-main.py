from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


l_paddle.shape("square")
r_paddle.shape("square")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer()






screen.listen()
screen.onkey(fun=l_paddle.move_up,key="Up")
screen.onkey(fun=l_paddle.move_down,key="Down")

screen.onkey(fun=r_paddle.move_up,key="w")
screen.onkey(fun=r_paddle.move_down,key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Collision with Right Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if Ball has gone out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
       

screen.exitonclick()
