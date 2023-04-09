import turtle as t
import time

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


start_pos = [(0, 0), (-20, 0), (-40, 0)]

segments = []

game_is_on = True
 
for position in start_pos:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)



while game_is_on:
    head = segments[0]
    screen.update()
    time.sleep(0.1)

    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
