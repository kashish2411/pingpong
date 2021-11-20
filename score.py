from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore, align="center",font=("Arial",75,"normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Arial", 75, "normal"))
    def r(self):
        self.rscore+=1
        self.update()
    def l(self):
        self.lscore+=1
        self.update()
