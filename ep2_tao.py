'''
Couse : Python for Beginners from Zero
EP.2 : By BenzSutee
'''

import turtle
tao = turtle.Turtle()
tao.shape('turtle')
tao.speed(50)

''' For move tao to position. '''
def tao_goto(x = 0, y = 0):
    tao.penup()
    tao.hideturtle()
    tao.home()
    tao.goto(x,y)
    tao.showturtle()
    tao.pendown()

''' For draw body of train. '''
def tao_body_train():
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

''' For draw hood of train. '''
def tao_hood_train():
    tao.left(90)
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

''' For draw window of train. '''
def tao_window_train(w = 20, h = 10):
    tao.forward(w)
    tao.left(90)
    tao.forward(h)
    tao.left(90)
    tao.forward(w)
    tao.left(90)
    tao.forward(h)

''' For draw wheel of train. '''
def tao_wheel_train(r = 30):
    tao.pen(pencolor='black', fillcolor='gray', pensize=3, speed=tao.speed())
    tao.begin_fill()
    tao.circle(r)
    tao.end_fill()
    tao.pensize(1)

# Draw train
pos_offset_x = [-650, -200, 250]
pos_offset_y = [-300, -50, 200]

for i in range(3):
    tao_offset_x = pos_offset_x[i]
    tao_offset_y = pos_offset_y[i]
    
    tao_goto(tao_offset_x, tao_offset_y)
    tao_body_train()

    tao_goto(tao_offset_x + 50, tao_offset_y + 140)
    tao_hood_train()

    tao_goto(tao_offset_x + 270, tao_offset_y + 100)
    tao_window_train(110, 80)

    tao_goto(tao_offset_x + 50, tao_offset_y + -40)
    tao_wheel_train(35)     # guide wheel

    tao_goto(tao_offset_x + 130, tao_offset_y + -40)
    tao_wheel_train(35)     # guide wheel

    tao_goto(tao_offset_x + 330, tao_offset_y + -40)
    tao_wheel_train(50)     # power wheel

tao.hideturtle()
