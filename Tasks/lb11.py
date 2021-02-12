import turtle
# 1
for i in range(8):
    turtle.forward(100)
    turtle.right(360/8)
    turtle.pendown()

# 2
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(8):
    turtle.forward(100)
    turtle.right(360/8)
    turtle.pendown()
turtle.end_fill()
turtle.pensize(5)
for i in range(8):
    turtle.forward(100)
    turtle.right(360/8)
    turtle.pendown()

# 3
def draw_star(size, points):
    for i in range(points):
        angle = 180.0 - 180.0 / points
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)


draw_star(150, 9)
turtle.mainloop()