from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update()

    def update(self):
        self.goto(100, 200)
        self.write(self.player1_score, align="center", font=("Courier", 75, "normal"))
        self.goto(-100, 200)
        self.write(self.player2_score, align="center", font=("Courier", 75, "normal"))

    def get_score1(self):
        self.player1_score+=1
        self.update()
    def get_score2(self):
        self.player2_score +=1
        self.update()