from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time
PADDLE_HEIGHT = 100 # 20 (default) * 5 (stretch_wid) = 100

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
#to listen to keystrokes
screen.listen()
#use the tracer method to turn off the animation
# so you don't see the paddle moving from the centre to the right hand side
screen.tracer(0)

r_paddle = Paddle(color = "white", x = 350, y = 0)
l_paddle = Paddle(color = "white", x = -350, y = 0)

#remember not to add the parentheses to the function: otherwise it won't work
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

ball = Ball()
scoreboard = Scoreboard()

#since we used the tracer method, we need to manually refresh the screen
#otherwise since we turned off our animation we won't be able to see
#our paddle that we created.
#we do that by using while loop and some sort of a variable

game_is_on = True
while game_is_on:
    screen.update()
    # Without a delay, the loop runs as fast as the CPU allows —
    # the ball/paddles will move far too fast to control:
    time.sleep(0.1)
    ball.move()  # on every update the ball moves

    #check if the ball is hitting the top or bottom walls
    #300 extended in each direction - the ball width
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check if the ball hitting the paddles
    if (ball.xcor() > 320 and abs(ball.ycor() - r_paddle.ycor()) < PADDLE_HEIGHT / 2) or \
   (ball.xcor() < -320 and abs(ball.ycor() - l_paddle.ycor()) < PADDLE_HEIGHT / 2):
        if ball.xcor() > 320:
            #to avoid ball bouncing behind the paddle with the wall
            ball.setx(320)
        if ball.xcor() < -320:
            ball.setx(-320)
        ball.bounce_x()
        ball.increase_speed()

    # check if the ball is passing the paddles and the screen boundry
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        #reset the ball position
        ball.reset_position(towards_right=False) # serve toward the player who won

    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset_position(towards_right=True)

screen.exitonclick()
