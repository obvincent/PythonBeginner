import colorgram
from turtle import Turtle, Screen, pos
import random
"""colours = colorgram.extract("hirst-painting\dhimage.jpg", 25)
colour_list = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    new_colour = (r, g, b)

    colour_list.append(new_colour)

print(colour_list)"""

colour_list = [(199, 168, 94), (227, 239, 232), (129, 179, 191), (163, 58, 78), (234, 221, 121), (49, 113, 167), (241, 217, 222), (104, 87, 83), (143, 187, 119), (239, 245, 249), (216, 151, 171), (67, 125, 76), (94, 124, 180), (85, 165, 94), (190, 71, 90), (161, 34, 49), (142, 119, 116), (221, 173, 182), (175, 205, 174), (163, 202, 211), (204, 116, 48), (75, 60, 56), (67, 56, 52), (176, 190, 213)]

#10 * 10
#Size 20, with 50 paces apart
#Paint dots using colour palate we created.

tony = Turtle()

#TODO 1: Set up Tony's speed, pen, and position
tony.speed("fastest")
tony.pensize(201)
tony.penup()

my_screen = Screen()
my_screen.colormode(255)

#TODO 2: Print a dot, then moves 50 spaces forward. After 10 dots, move up a line.
for lines in range(10):

    tony.setpos(-250, -250 + 50*(lines))
    
    for dots in range (10):
        tony.pendown()
        tony.dot(25, random.choice(colour_list))
        tony.penup()
        tony.forward(50)




my_screen.exitonclick()

#print(pos(tony))
