import turtle


def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)


def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)


def house_boat(width, height):
    rectangle(width, 1/2*height)
    turtle.forward(1/2*width-1/2*height)
    square(height)
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    triangle(height)


turtle.color("orange")
house_boat(150, 50)
turtle.penup()
turtle.forward(-400)

turtle.color("blue")
turtle.pendown()
house_boat(250, 100)
turtle.Screen().exitonclick()
