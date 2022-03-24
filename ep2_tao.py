import turtle
tao = turtle.Pen()  # ดึงความสามารถการใช้ปากกา
tao.shape('turtle') # แปลงรางเป็นเต่า

def rectangle():
    ''' ฟังก์ชั่นนี้เอาไว้วาดรูปสี่เหลี่ยม '''
    for i in range(4):
        tao.fd(100)
        tao.lt(90)

def go(x, y):
    ''' ฟังก์ชั่นนี้เอาไว้ย้ายตำแหน่งเต่า '''
    tao.penup()
    tao.goto(x, y)
    tao.pendown()

go(-100,50)
rectangle()
go(0, -100)
rectangle()
