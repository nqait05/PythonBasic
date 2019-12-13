import turtle
import math


# in this file, i define some function to draw some basic image #
# draw_santa_house , draw_dashed_line, draw_star, draw_hexagon or honeycomb ( combine 6 hexagon) #


def draw_santa_house(length=100):
    # draw the house of santa claus with given edg, defaut is 100 #

    cross = math.sqrt(2) * edglong
    turtle.forward(edglong)
    turtle.left(90)
    turtle.forward(edglong)
    turtle.left(90)
    turtle.forward(edglong)
    turtle.left(90)
    turtle.forward(edglong)

    turtle.left(135)
    turtle.forward(cross)
    turtle.left(90)
    turtle.forward(cross / 2)
    turtle.left(90)
    turtle.forward(cross / 2)
    turtle.left(90)
    turtle.forward(cross)


def draw_dashed_line():
    # draw a dashed line
    for i in range(10):
        turtle.forward(15 + i * 5)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()


def line_without_moving(length=50):
    turtle.forward(length)
    turtle.backward(length)


def star_arm():
    line_without_moving()
    turtle.right(360 / 5)


def draw_star(length=50):
    # draw star
    for _ in range(5):
        star_arm()


# draw hexagon
def draw_hexagon(length=100):
    for _ in range(6):
        turtle.forward(length)
        turtle.left(360 / 6)


def draw_honeycomb(length=100):
    # draw HoneyComb
    for _ in range(6):
        draw_hexagon(length)
        turtle.forward(length)
        turtle.right(60)


draw_honeycomb(10)
