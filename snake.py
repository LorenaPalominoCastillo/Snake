#Codigo modificado por:
#Autor: Emilio Campuzano Mejia
#Autor: Lorena Palomino Castillo

from turtle import *
from random import randrange
from freegames import square, vector
import random

serpiente = ["blue","yellow","green","orange","magenta"]
Colors = random.choice(serpiente)
comida = ["blue","yellow","green","orange","magenta"]
Colorc = random.choice(comida)

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
    head.move(aim)#aqui
    xf = random.randint(-1,1) * 10
    yf = random.randint(-1,1) * 10
    aim2 = vector(xf, yf)
    food.move(aim2)


    if not inside(head) or head in snake: #aqui
        square(head.x, head.y, 9, 'red')
        update()
        return

    if not inside(food) or food in food:
        square(food.x, food.y, 9, 'red')
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
        square(body.x, body.y, 9, (Colors))

    for i in food:
        square(food.x, food.y, 9, (Colorc))


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
