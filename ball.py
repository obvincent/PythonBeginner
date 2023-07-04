from turtle import Turtle
import random
y_direction = [1,-1]
#width = 20
#height = 20
#x_pos = 0
#y_pos = 0

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("normal")
        self.right(45)
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
    
    def wall_bounce(self):
        self.ymove = -1*self.ymove
    
    def paddle_bounce(self):
        self.xmove *= -1
    
    def reset_position(self):
        if self.xcor() == 390 or self.xcor() == -390:
            self.goto(0, 0)
            self.xmove *= -1
            self.ymove *= random.choice(y_direction)
        


