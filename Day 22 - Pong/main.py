import turtle as t
import time
from paddle import Paddle


screen = t.Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))



screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()