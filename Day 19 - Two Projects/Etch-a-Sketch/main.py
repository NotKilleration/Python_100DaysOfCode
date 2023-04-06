import turtle as t


screen = t.Screen()


def forward():
    t.forward(10)

def backward():
    t.backward(10)

def clockwise():
    t.right(10)

def counter_clockwise():
    t.left(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()




screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(clockwise, "Right")
screen.onkey(counter_clockwise, "Left")
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(forward, "W")
screen.onkey(backward, "S")
screen.onkey(clockwise, "D")
screen.onkey(counter_clockwise, "A")
screen.onkey(clear_screen, "C")
screen.onkey(clear_screen, "c")



screen.listen()
screen.exitonclick()