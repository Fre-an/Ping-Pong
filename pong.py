import turtle
import random
import time
import threading

dis = turtle.Screen()
dis.title("PONG")
dis.bgcolor("black")
dis.setup(width = 800, height = 600)
dis.tracer(0)

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.shapesize(stretch_wid= 5, stretch_len= 1)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.penup()
paddle2.goto(350, 0)
paddle2.shapesize(stretch_wid= 5, stretch_len= 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

dx = 0.3
dy = 0.3

# Paddles moving
def paddle1up():
    y = paddle1.ycor()
    if y == 240:
        paddle1.sety(240)
    else:
        y += 20
        paddle1.sety(y)

def paddle1down():
    y = paddle1.ycor()
    if y == -240:
        paddle1.sety(-240)
    else:
        y -= 20
        paddle1.sety(y)

def paddle2up():
    y = paddle2.ycor()
    if y == 240:
        paddle2.sety(240)
    else:
        y += 20
        paddle2.sety(y)

def paddle2down():
    y = paddle2.ycor()
    if y == -240:
        paddle2.sety(-240)
    else:
        y -= 20
        paddle2.sety(y)

# Keyboard
dis.listen()
dis.onkeypress(paddle1up, "w")
dis.onkeypress(paddle1down, "s")
dis.onkeypress(paddle2up, "Up")
dis.onkeypress(paddle2down, "Down")

# Score
score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0, 260)
score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
score.hideturtle()
score1 = 0
score2 = 0

# Game
while True:
    dis.update()
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if ball.ycor() > 290:
        dy *= -1

    if ball.ycor() < -290:
        dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50)):
        ball.setx(340)
        dx *= -1

    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50)):
        ball.setx(-340)
        dx *= -1

    if score1 == 3:
        score.clear()
        score.write("Player 1 won!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        dx = 0
        dy = 0
    
    if score2 == 3:
        score.clear()
        score.write("Player 2 won!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        dx = 0
        dy = 0