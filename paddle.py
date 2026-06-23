from turtle import Turtle
#max height a paddle can reach
MAX_HEIGHT_PADDLE = 250
PADDLE_MOVEMENT_UNIT = 20


class Paddle(Turtle):
    def __init__(self,color,x,y):
        super().__init__()
        self.color(color)
        self.shape("square")
        #all turtles start off as 20x20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x,y)

    def move_up(self):
        if self.ycor() + PADDLE_MOVEMENT_UNIT<= MAX_HEIGHT_PADDLE:
            self.goto(self.xcor(), self.ycor()+PADDLE_MOVEMENT_UNIT)
        if self.ycor() + PADDLE_MOVEMENT_UNIT >= MAX_HEIGHT_PADDLE:
            self.goto(self.xcor(), MAX_HEIGHT_PADDLE)

    def move_down(self):
        if self.ycor() - PADDLE_MOVEMENT_UNIT >= -MAX_HEIGHT_PADDLE:
            self.goto(self.xcor(), self.ycor()-PADDLE_MOVEMENT_UNIT)
        if self.ycor() - PADDLE_MOVEMENT_UNIT <= -MAX_HEIGHT_PADDLE:
            self.goto(self.xcor(), -MAX_HEIGHT_PADDLE)
