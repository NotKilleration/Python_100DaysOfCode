import turtle as t
import random

# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

t.colormode(255)
colors = [(17, 246, 202), (239, 193, 82), (84, 56, 67), (193, 242, 44), (110, 107, 146), (129, 203, 88), (174, 236, 63), (217, 82, 78), (187, 82, 219), (166, 231, 99), (29, 44, 152), (120, 169, 82), (29, 232, 148), (207, 80, 229), (82, 136, 12), (82, 221, 195), (187, 158, 74), (13, 189, 117), (34, 75, 105), (106, 40, 105), (98, 200, 204), (37, 162, 204), (244, 162, 41), (60, 101, 44), (210, 209, 150), (170, 28, 92), (76, 28, 183), (41, 92, 15), (151, 220, 206), (110, 77, 61), (153, 75, 178), (204, 99, 178), (23, 126, 167), (54, 105, 9), (220, 138, 197), (200, 11, 73), (68, 97, 219), (215, 80, 131), (176, 124, 37), (129, 201, 217), (11, 92, 109), (70, 22, 152), (192, 97, 53), (201, 56, 170), (12, 28, 169), (50, 30, 10), (179, 154, 239), (155, 149, 42), (147, 220, 103), (23, 206, 27)]



t.speed("fastest")
t.pensize = 20
x = 0
t.setheading(225)
t.penup()
t.forward(250)
t.setheading(0)
t.hideturtle()

for i in range(10):

    for i in range (10):

        t.dot(20, random.choice(colors))
        t.forward(50)


    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.right(90)
    t.forward(20)
    t.right(90)
    x += 20


screen = t.Screen()
screen.exitonclick()
