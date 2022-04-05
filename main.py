import time
from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

player1 = Player((350, 0))
player2 = Player((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# Player1

screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")

# Player2
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.get_score2()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.get_score1()


# time.sleep(0.1)
screen.exitonclick()
