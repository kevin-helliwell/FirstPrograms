import turtle


def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


def octagon(length):
    for i in range(8):
        turtle.forward(length)
        turtle.left(45)


def stop(length):
    octagon(length)
    turtle.forward(3/8*length)
    rectangle(1/5*length, 2*length)

# Test
# octagon(50)
# rectangle(50, 100)
# turtle.color("red")
# stop(50)
# turtle.penup()
# turtle.forward(200)
# turtle.pendown()
# turtle.color("blue")
# stop(100)

# turtle.Screen().exitonclick()
