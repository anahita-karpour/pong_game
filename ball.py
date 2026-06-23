from turtle import Turtle

BALL_MOVEMENT_UNIT = 10
ANGLE = 45


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.move_distance = BALL_MOVEMENT_UNIT
        self.setheading(ANGLE) # Sets the direction once
        self.penup()

    def move(self):
        self.forward(self.move_distance) # moves the turtle forward
        # to the direction the turtle is facing

    def increase_speed(self):
        self.move_distance += 5

    def bounce_y(self):
        # bounce off the top and bottom walls
        self.setheading(360 - self.heading())

    def bounce_x(self):
        # bounce off the paddles
        #make the ball move the opposite direction to serve the player who lost
        self.setheading(180 - self.heading())

    def reset_position(self, towards_right =True):
        self.setposition(0,0)
        self.setheading(ANGLE if towards_right else 180- ANGLE)
        #reset the speed
        self.move_distance = BALL_MOVEMENT_UNIT

