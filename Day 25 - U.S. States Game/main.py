import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()



# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
# screen.exitonclick()