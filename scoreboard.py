from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup
        self.goto(0,270)
            
    def add_to_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
