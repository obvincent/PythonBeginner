from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

ball_speed = 0.09
#The Screen
my_screen = Screen()
my_screen.setup(width = 800, height=600) 
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

#The Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_down, "s")

#The Ball
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    my_screen.update()
    ball.move()
    
    #Detect Collision with the wall
    if ball.ycor()>= 280 or ball.ycor()<= -280:
        ball.wall_bounce()

    #Detect Collision with the paddles
    if ball.xcor() == 330 and ball.distance(r_paddle) < 53.86 or (ball.xcor() == -330 and ball.distance(l_paddle) < 53.86):
        ball.paddle_bounce()
        ball_speed *= 0.80
    
    #Reset Ball and Score When Out of Bounds
    if ball.xcor() == 390:
        ball.reset_position()
        scoreboard.l_point()
        ball_speed = 0.09

    elif ball.xcor() == -390:
        ball.reset_position()
        scoreboard.r_point()
        ball_speed = 0.09

    if scoreboard.r_score == 2 or scoreboard.l_score == 2:
        game_is_on = False
        scoreboard.game_over()

my_screen.exitonclick()
