import turtle
import random

def drunken_move_w():
    turtle.setheading(0)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_a():
    turtle.setheading(0)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_s():
    turtle.setheading(0)
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(drunken_move_w,'w')

turtle.onkey(drunken_move_a,'a')
turtle.onkey(drunken_move_s,'s')
turtle.onkey(drunken_move_d,'d')

turtle.onkey(restart,'Escape')
turtle.listen()

turtle.exitonclick()
