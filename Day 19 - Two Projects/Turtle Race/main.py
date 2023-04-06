import turtle as t
import random

is_race_on = False

screen = t.Screen()
screen.setup(width = 500, height = 400)
user_bet = t.textinput(title = "Make your bet!", prompt = "Which turtle do you want to put your bet on?")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
x = -230
y = -70

for turtle_index in range(0, 6):

    new_turtle = t.Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 30
    # a.size = 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost. The {winner} turtle is the winner.")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)    
    
screen.exitonclick()
