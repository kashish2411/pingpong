from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score
b=Ball()
scoreB=Score()

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(height=600,width= 800)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up_go, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up_go, "w")
screen.onkey(l_paddle.down, "s")
score_r=0
score_l=0
game_on = True
while game_on:
    time.sleep(b.ms)
    screen.update()
    b.move()
    if ( (b.ycor()>280) or (b.ycor() < -280) ):
        b.bounce_ball()
    if (b.distance(r_paddle)<70 and b.xcor()>320 or b.distance(l_paddle)<80 and b.xcor()<-310):
        b.bounce()
    if b.xcor()>380:
        b.resetpos()
        scoreB.l()
    if b.xcor()<-380:
        b.reset()
        scoreB.r()








screen.exitonclick()
