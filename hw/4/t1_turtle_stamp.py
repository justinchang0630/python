"""
Topic:請使用turtle及loop印出下列圖形

e.g.
turtle_stamp.jpg
"""
import turtle
for __ in range(5):
    turtle.stamp()
    turtle.penup()
    turtle.forward(150)
    turtle.stamp()
    turtle.home()
    turtle.right(70)