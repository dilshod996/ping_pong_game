from turtle import Turtle


MOVING_DISTANCE = 30

class Player(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + MOVING_DISTANCE
        x_pos = self.xcor()
        self.goto(x_pos, new_y)
        print("wl")

    def go_down(self):
        new_y = self.ycor() - MOVING_DISTANCE
        x_pos = self.xcor()
        self.goto(x_pos, new_y)








    # def creating_paddle(self):
    #     paddle = Turtle(shape="square")
    #     paddle.color("white")
    #     paddle.shapesize(stretch_wid=4, stretch_len=1)
    #     paddle.penup()
    #     paddle.goto(350, 0)
    #
    # def move(self):
    #     self.paddle.xcor(380, -380)
    #     self.paddle.forward(20)
