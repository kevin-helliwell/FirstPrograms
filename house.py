import turtle


def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)


def house(length):
    triangle(length)
    square(length)


turtle.color("red")
house(100)
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.color("blue")
house(50)

turtle.Screen().exitonclick()
