'''
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle
def tree_leaves(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.setheading(0)
	turtle.color('red')
	turtle.begin_fill()
	turtle.forward(40)
	turtle.left(120)
	turtle.forward(40)
	turtle.left(120)
	turtle.forward(40)
	turtle.end_fill()
def tree_trunk(x, y):
    turtle.penup()
    turtle.goto(x+12.5, y)
    turtle.pendown()
    turtle.color('green')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()
k = 0
for i in range(1,11):
    tree_leaves(k,0)
    tree_trunk(k,0)
    k = k +20