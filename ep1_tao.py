'''
Couse : Python for Beginners from Zero
EP.1 : By BenzSutee
'''

import turtle
#s = turtle.getscreen()
tao = turtle.Turtle()
tao.shape('turtle')
tao_offset_x = -200
tao_offset_y = 0
tao.penup()
tao.goto(tao_offset_x, tao_offset_y)
tao.pendown()

# Draw body of train.
tao.forward(400)
tao.left(90)
tao.forward(200)
tao.left(90)
tao.forward(150) 
tao.left(90)
tao.forward(60)
tao.right(90)
tao.forward(250)
tao.left(90)
tao.forward(140)

# Draw hood of train.
tao.penup()
tao.goto(tao_offset_x + 50, tao_offset_y + 140)
tao.left(180)
tao.pendown()

tao.forward(50)
tao.left(90)
tao.forward(10)
tao.right(90)
tao.forward(5)
tao.right(90)
tao.forward(50)
tao.right(90)
tao.forward(5)
tao.right(90)
tao.forward(10)
tao.left(90)
tao.forward(50)

# Draw windows of train.
tao.penup()
tao.goto(tao_offset_x + 270,tao_offset_y + 100)
tao.pendown()

tao.left(180)
tao.forward(80)
tao.right(90)
tao.forward(110)
tao.right(90)
tao.forward(80)
tao.right(90)
tao.forward(110)

# Draw wheel-1 of train.
tao.penup()
tao.home()
tao.goto(tao_offset_x + 50,tao_offset_y + -40)
tao.pendown()

tao.pen(pencolor='black', fillcolor='gray', pensize=3, speed=9)
tao.begin_fill()
tao.circle(35)
tao.end_fill()

# Draw wheel-2 of train.
tao.penup()
tao.home()
tao.goto(tao_offset_x + 130, tao_offset_y + -40)
tao.pendown()

tao.pen(pencolor='black', fillcolor='gray', pensize=3, speed=9)
tao.begin_fill()
tao.circle(35)
tao.end_fill()

# Draw wheel-3 of train.
tao.penup()
tao.home()
tao.goto(tao_offset_x + 330,tao_offset_y + -40)
tao.pendown()

tao.pen(pencolor='black', fillcolor='gray', pensize=3, speed=9)
tao.begin_fill()
tao.circle(50)
tao.end_fill()

