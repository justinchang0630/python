import turtle
import time

for x in range(60):
    turtle.penup
    time.sleep(1)
    turtle.right(6*x)
    turtle.stamp()
    turtle.forward(150)
    print (x)
    turtle.home()
    turtle.clear()


