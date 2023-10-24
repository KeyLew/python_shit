# import turtle
# import random
# import time
# import math
# colors = ["red", "blue", "black", "green"]
# count = 0
# length = 50
# howFarToMove = length
# def drawhex():
#     turtle.pencolor(random.choice(colors))
#     turtle.speed(0)
#     turtle.pendown()
#     turtle.forward(length)
#     turtle. left(300)
#     turtle.forward(length)
#     turtle. left(300)
#     turtle.forward(length)
#     turtle. left(300)
#     turtle.forward(length)
#     turtle. left(300)
#     turtle.forward(length)
#     turtle. left(300)
#     turtle.forward(length)
#     turtle. left(300)
#     turtle.penup()
# def drawTriangle():
#     turtle.pencolor(random.choice(colors))
#     turtle.speed(0)
#     turtle.pendown()
#     turtle.forward(length)
#     turtle.left(119)
#     turtle.forward(length)
#     turtle.left(119)
#     turtle.forward(length)
#     turtle.left(119)
#     # turtle.penup()
# def drawsquare():
#     turtle.pencolor(random.choice(colors))
#     turtle.speed(0)
#     turtle.pendown()
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.penup()
# def drawstar():
#     turtle.pencolor(random.choice(colors))
#     turtle.speed(0)
#     turtle.pendown()
#     turtle.forward(length)
#     turtle. left(72)
#     turtle.forward(length)
#     turtle.right(144)
#     turtle.forward(length)
#     turtle. left(72)
#     turtle.forward(length)
#     turtle.right(144)
#     turtle.forward(length)
#     turtle. left(72)
#     turtle.forward(length)
#     turtle.right(144)
#     turtle.forward(length)
#     turtle. left(72)
#     turtle.forward(length)
#     turtle.right(144)
#     turtle.forward(length)
#     turtle. left(72)
#     turtle.forward(length)
#     turtle.right(144)
#     turtle.forward(length)
#     turtle. left(72)
#     turtle.forward(length)
#     turtle.penup()
# def drawspiral():
#     turtle.color(colors)
#     turtle.forward(length )
#     turtle.left(59)

# while True:
#     drawspiral
#     # drawTriangle()
#     # turtle.left()
#     # drawsquare()
#     # drawhex()
#     # drawstar()
#     # turtle.forward(howFarToMove)
#     length += 1
#     # howFarToMove += 2

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()