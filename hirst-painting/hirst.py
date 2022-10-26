# import colorgram
# colors = colorgram.extract("image.jpg",30)
# my_list=[]
# for color in colors:
#     RGB = color.rgb
#     my_tuple = (RGB.r, RGB.g, RGB.b)
#     my_list.append(my_tuple)
#
# ass = print(my_list)


ass =[(20, 117, 159), (164, 58, 91), (228, 160, 73), (212, 127, 152), (210, 75, 103), (36, 126, 82), (239, 212, 220), (114, 173, 203), (216, 164, 18), (228, 72, 56), (214, 233, 223), (207, 224, 235), (230, 199, 130), (157, 26, 51), (8, 106, 71), (166, 72, 43), (121, 182, 151), (24, 168, 185), (234, 163, 180), (60, 160, 126), (242, 166, 155), (26, 60, 119), (26, 55, 89), (9, 88, 108), (153, 211, 194), (82, 34, 57), (149, 208, 218), (180, 185, 216), (113, 116, 169)]
from turtle import Turtle,Screen
import random

matt = Turtle()
screen = Screen()

screen.bgcolor("black")
matt.color("white")

screen.colormode(255)

matt.penup()
matt.goto(-90,-90)
i=-90
for k in range(10):
    for _ in range(10):
        matt.dot(20)
        matt.forward(50)
        matt.pencolor(random.choice(ass))
    i+=50
    matt.setposition(-90,i)

screen.exitonclick()
