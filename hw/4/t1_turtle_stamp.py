"""
Topic:請使用turtle及loop印出下列圖形
e.g.
turtle_stamp.jpg
"""
import turtle
turtle.penup()
turtle.speed(0)
for a in range(9):
    turtle.forward(150)
    turtle.stamp()
    turtle.home()
    turtle.right(45*a)