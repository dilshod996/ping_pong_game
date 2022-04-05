from turtle import Turtle
LINE_POSITIONS = [(0, 0), (0, 60), (0, -60), (0, 120), (0, -120), (0, 180), (0, -180), (0, 240), (0, -240)]

class Line:
    def __init__(self):

        self.all_lines = []
        self.creating_lines()

    def creating_lines(self):

        for position in LINE_POSITIONS:
            line = Turtle(shape="square")
            line.penup()
            line.color("white")
            line.shapesize(stretch_wid=1.2, stretch_len=0.5)
            line.goto(position)
            self.all_lines.append(line)