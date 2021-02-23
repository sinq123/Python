
#turtle模块的简单应用




import math
import turtle

def drawcircle(x, y, r):
    turtle.up() #提起笔，不落点
    turtle.setpos(x+r, y) # 设定第一个点的位置
    turtle.down() # 下笔

    for i in range(0, 365, 5): #以+5为长度，运行到i=365
        a = math.radians(i) #度数转化为弧度
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a)) # 画⚪

drawcircle(100, 100, 50)
turtle.mainloop()