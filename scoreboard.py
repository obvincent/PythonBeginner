from turtle import Turtle
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update()
    
    def update(self):
        self.clear()
        self.score += 1
        self.goto(-250, 250)
        self.write(f"Level = {self.score}", True, align = "left", font = FONT)
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.write("GAME OVER", True, align = "center", font = FONT)


        
