import turtle

turtle.color('red')
turtle.shape('turtle')
turtle.penup()
for step in range(5,100,1):
    turtle.stamp()
    turtle.forward(step)
    turtle.right(25)
    print(step)