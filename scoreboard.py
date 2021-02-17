from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as data:
            high_score = data.read()
            if high_score == "":
                self.high_score = 0
            else:
                self.high_score = int(high_score)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def add_to_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score = {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )
