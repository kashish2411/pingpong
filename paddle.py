from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(10, 2)
        self.color("white")
        self.penup()
        self.setposition(pos)

    def up_go(self):
        y = int(self.ycor() + 20)
        self.goto(self.xcor(), y)

    def down(self):
        y = int(self.ycor() - 20)
        self.goto(int(self.xcor()), y)
