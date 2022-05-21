import turtle


# (1) Draw a line

# turtle.shape("turtle")
# turtle.speed(0)

# turtle.forward(90)
# turtle.left(90)
# turtle.forward(90)
#
# turtle.Screen().exitonclick()

# (2) Draw a square
# turtle.color("orange")
# turtle.width(10)
# turtle.speed(5)
# for i in range(4):
#     turtle.forward(90)
#     turtle.left(90)
# turtle.Screen().exitonclick()

# (3) Draw two squares
# turtle.color("blue")
# turtle.width(10)
# turtle.speed(0)
# for i in range(4):
#     turtle.forward(90)
#     turtle.left(90)
# turtle.penup()
# turtle.forward(180)
# turtle.pendown()
# turtle.color("red")
# turtle.width(10)
# turtle.speed(0)
# for i in range(4):
#     turtle.forward(90)
#     turtle.left(90)
# turtle.penup()
# turtle.color("blue")
# turtle.forward(-90)
# turtle.Screen().exitonclick()

# (4) Create a square function
def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)


# # Test
# square(50)
# square(100)
# turtle.Screen().exitonclick()

# (5) Create a rectangle function
def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


# rectangle(40, 50)
# rectangle(100, 110)
# turtle.Screen().exitonclick()

# Draw a picture
# turtle.speed(0)
# for j in range(10):
#     turtle.pensize(.2*j)
#     turtle.color("yellow")
#     square(j)
#     rectangle(2 * j, 2 * (j + 2))
#     turtle.color("blue")
#     square(3 * j)
#     rectangle(4*j, 4*(j+4))
#     turtle.color("orange")
#     square(5*j)
#     rectangle(6 * j, 6 * (j + 6))
#     turtle.color("green")
#     square(7 * j)
#     rectangle(8*j, 8*(j+8))
#     turtle.color("purple")
#     square(9*j)
#     rectangle(10 * j, 10 * (j + 10))
# turtle.Screen().exitonclick()
