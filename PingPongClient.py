# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:18:27 2019

@author: M7md_Karam
"""
#For GUI
from turtle import Turtle, Screen
#For Communication.
from socket import socket, AF_INET, SOCK_STREAM
#For Multi-threading.
from _thread import start_new_thread

def receive_thread(s):
    while True:
        y = s.recv(500).decode('UTF-8')
        paddle_a.sety(y)

def send_function(y):
    s.send(str(y).encode('UTF-8'))

wind = Screen()
wind.title("Ping Pong: Client Side")
wind.bgcolor("#222222")
wind.setup(width=800, height=600)
wind.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = -.5

# Pen
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0          Player B: 0", align="center", font=("Comic Sans MS", 15, "normal"))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    send_function(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    send_function(y)

# Keyboard binding
wind.listen()
wind.onkeypress(paddle_a_up, "w")
wind.onkeypress(paddle_a_down, "s")
wind.onkeypress(paddle_b_up, "Up")
wind.onkeypress(paddle_b_down, "Down")

s=socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1',7010))
#create thread for serving that session.
start_new_thread(receive_thread,(s,))

# Main game loop
while True:
    wind.update()

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

	# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}          Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 15, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}          Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 15, "normal"))

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40:
        ball.setx(-340)
        ball.dx *= -1
        
        
