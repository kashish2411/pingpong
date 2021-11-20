from turtle import Turtle
class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.penup()
        self.goto(0,0)
        self.xm=3
        self.ym=3
        self.ms=0.05


    def move(self):
        x = self.xcor()+self.xm
        y = self.ycor()+self.ym
        self.goto(x,y)
    def bounce_ball(self):
           self.ym*=-1

    def bounce(self):
        self.xm *= -1
        self.ms*=0.05
    def resetpos(self):
        self.goto(0,0)
        self.ms=0.05
        self.bounce()
    def reset(self):
        self.goto(0, 0)
        self.ms=0.05
        self.bounce_ball()


