from turtle import *
from math import *
#学号处理
name = input("请输入学号:")
#name = '111809001182'
x2 = int(name[0:3])
#x2是输入学号的前3位转化为的数字
y2 = int(name[9:12])
#y2是输入学号的9-12位转化为的数字
if x2  > 400:
    x2 = x2//400
elif y2 > 400:
    y2 = y2//400
elif x2 %2 == 1:
    x2 = -x2
elif y2 %2 == 1:
    y2 = -y2
#//是除法取整的意思，比如，7//3，7除以3，等于2余1，所以7//3=2；下边的%是取余，即
#7%3=1
#'#'是注释，=是赋值，==是判断。上边一段if else是给x2y2做一些转换
#坐标系处理
t1 = Turtle()
t2 = Turtle()
#Turtle是绘图工具，下边这些都是它里边的方法。speed是速度，fd是移动到，seth是箭头朝向
#下边这一段就是画x轴y轴。penup是抬起笔，goto是移动到，然后pendown是放下笔，up-移动-放下
#笔是不挨画布的，所以就没有连线，这里pendown之后，后边for循环里再移动的时候就会有线了
t1.speed(50)
t2.speed(10)
t1.fd(-300)
t1.fd(600)
t2.seth(90)
t2.fd(-300)
t2.fd(600)
t2.penup()
t2.goto(x2,y2)
t2.pendown()
#追赶
x1 = 0
y1 = 0
#x1,y1是原点0,0
v1 = 15
v2 = 3
th1 = 0
th2 = 0
step = 0.1
#这个for循环是目的是为了不停的计算这两个点之间的距离和角度，两点之间直线最短，所以就
#一直调整th1这个角度，来向着x2,y2这个点移动。cos，sin这些就是数学里的三角函数
for i in range(1000):
    x1 += v1 * cos(th1)*step
    y1 += v1 * sin(th1)*step
    x2 += v2 * cos(th2)*step
    y2 += v2 * sin(th2)*step
    t1.goto(x1,y1)
    #t2.penup()
    #t2.pendown()
    t2.goto(x2,y2)
    #t2.penup()
    t2.seth(0)
    t1.pencolor('red')
    t2.pencolor('black')
#求下一次的方向
    if((y2-y1)>1e-10 and (x2-x1)>1e-10):
        th1=atan(y2-y1)/(x2-x1)
    elif((y2-y1)>1e-10 and (x2-x1)<-1e-10):
        th1= pi+atan((y2-y1)/(x2-x1))
    elif((x2-y1)<-1e-10 and (x2-y1)>1e-10):
        th1=atatan((y2-y1)/(x2-x1))
    else:
        th1=-pi+atan((y2-y1)/(x2-x1))
    if(sqrt(pow(x2-x1,2)+pow(y2-y1,2)) < 0.5):
        break
#终止的条件就是两点之间的距离小于0.5如果速度过快，还没来得及计算距离就走掉了，就不会重合了。
#step是步进，就是移动的快慢的意思。break是停止循环，不再执行.sqrt是开平方的运算,
#pow是幂运算，参数有两个，即x的y次幂。
#break之后，继续执行下边的打印。打印的是计算的时间和距离。打印\t是换行符号
print(str(i*step)+"s")
print('\t')
print=(str(sqrt(pow(x2-x1,2)+pow(y2-y1,2)))+"m")
