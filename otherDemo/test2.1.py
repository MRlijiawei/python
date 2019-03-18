import turtle,datetime,time

turtle.speed(0)
turtle.Turtle().screen.delay(0)

def drawGap():
    turtle.penup()
    turtle.fd(5)
    
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
def drawDight(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    turtle.hideturtle()
    
def drawDate(date):
    turtle.(0)
    #turtle.Turtle().screen.delay(0)
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('点',font=("Arial", 18 ,"normal"))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('分',font=("Arial",  18, "normal"))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('秒',font=("Arial", 18 ,"normal"))
        else:
            drawDight(eval(i))
        turtle.hideturtle()
        #turtle.update()

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    #drawDate(datetime.datetime.now().strftime('%H-%M=%S+'))
    #turtle.getscreen(drawDate(datetime.datetime.now().strftime('%S')))
                     
    for m in range(20):
        if m<20:
            #turtle.speed(0)
            drawDate(datetime.datetime.now().strftime('%H-%M=%S+'))
            turtle.hideturtle()
            turtle.fd(-500)
            time.sleep(1)
            #turtle.speed(0)
            turtle.clear()
        else:
            break

main()
