import turtle

turtle.penup()
turtle.goto(0,300)
turtle.pendown()

count = 6
while(count > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.left(180)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    count = count - 1

turtle.penup()
turtle.goto(0,300)
turtle.down()
turtle.right(90)

count = 6
while(count > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.left(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    count = count - 1

turtle.exitonclick()
