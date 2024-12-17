from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

l_paddle_coordinates = (-350,0)
r_paddle_coordinates = (350,0)

l_paddle = Paddle(l_paddle_coordinates)
r_paddle = Paddle(r_paddle_coordinates)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #Detection with the wall
  if ball.ycor() >280 or ball.ycor()<-280:
     ball.bounce_y()

     #Detect collision with both paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)< 50 and ball.xcor()< -320:
      ball.bounce_x()


      #detect ball when ball beyond right ball
  if ball.xcor() >380:
      ball.reset()
      scoreboard.l_point()

      #detect ball when ball beyong left wall
  if ball.xcor() <-380:
      ball.reset()
      scoreboard.r_point()


screen.exitonclick()