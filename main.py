import colorgram
# rgb_colors = []
# colors = colorgram.extract('Hirst_Photo.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(34, 108, 167), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 
152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192)]

from turtle import *
from random import randint

t = Turtle()
screen = Screen()

t.penup()
x = 0
t.speed('fastest')
screen.colormode(255.00)

for i in range(10):
    t.goto(-200, x)
    for j in range(10):
        t.dot(20, color_list[randint(0, len(color_list) - 1)])
        t.fd(50)
        x += 5
# t.dot(20, 'red')
# t.penup()
# t.fd(50)



screen.exitonclick()