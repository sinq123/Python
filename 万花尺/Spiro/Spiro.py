    #实现万花尺的功能
import math
import turtle
import sys, random, argparse
import numpy as np
import random
from PIL import Image
from datetime import datetime
from fractions import gcd

#定义Spiro 绘制曲线 利用定时器和update()，产生随机螺线。
#为了绘制Spiro对象并产生动画，将使用SpiroAnimator类
class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        #创建turtle对象
        self.t = turtle.Turtle()
        #设置光标形状
        self.t.shape('turtle')
        #设置定时器时常
        self.step = 5
        #设置绘图标记
        self.drawingComplete = False
        #调用参数
        self.setparams(xc, yc, col, R, r, l)
        self.restart()

    #螺旋图参数
    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.col = col
        self.R = int(R)
        self.r = int(r)
        self.l = l
        #通过与GCD相除，将r/R降低到最小值
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        #计算两个半径比
        self.k = float(r) / float(R)
        # 设置颜色
        self.t.color(*col)
        #保存当前角度
        self.a = 0

    #重新绘制图纸
    def restart(self):
        #设置绘图标记
        self.drawingComplete = False
        #显示turtle
        self.t.showturtle()
        #设置第一点
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1-k) * math.cos(a) + l * k * math.cos((1-k) * a/k))
        y = R * ((1-k) * math.sin(a) - l * k * math.sin((1-k) * a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    #连续绘制曲线
    def draw(self):
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot, self.step):
            a = math.radians(i) #度数转化为弧度
            x = R * ((1-k) * math.cos(a) + l * k * math.cos((1-k) * a/k))
            y = R * ((1-k) * math.sin(a) - l * k * math.sin((1-k) * a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        #隐藏光标
        self.t.hideturtle()

    #创建动画
    def update(self):
        #绘画完成，则无动画
        if self.drawingComplete:
            return 
        #增加角度值
        self.a += self.step
        R, k, l = self.R, self.k, self.l
        a = math.radians(self.a) #度数转化为弧度
        x = R * ((1-k) * math.cos(a) + l * k * math.cos((1-k) * a/k))
        y = R * ((1-k) * math.sin(a) - l * k * math.sin((1-k) * a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        #如果绘制完成， 设置标志为True
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            #隐藏光标
            self.t.hideturtle()

    #清除所以
    def clear(self):
        self.t.clear()


#SpiroAnimator类
class SpiroAnimator:
    def __init__(self, N):
        #以毫秒设置定时器的值
        self.deltaT = 10
        #获取窗口大小
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        #创建spiro对象
        self.spiros = []
        for i in range(N):
            #生成随机数
            rparams = self.genRandomParams()
            #
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            #设置turtle调用updata()时间
            turtle.ontimer(self.update, self.deltaT)

    #获取随机数
    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random())
        return (xc, yc, col , R, r, l)
    
    #重新启动
    def restart(self):
        for spiro in self.spiros:
            #清空
            spiro.clear()
            #生成随机数
            rparams = self.genRandomParams()
            spiro.setparams(*rparams)
            spiro.restart()

    #以动画的形式更新所以Spiro对象
    def update(self):
        nComplete = 0
        for spiro in self.spiros:
            spiro.update()
            #是否绘制完成
            if spiro.drawingComplete:
                nComplete +=1
        #完成次数等于线条总数
        if nComplete == len(self.spiros):
            self.restart() #重制
        turtle.ontimer(self.update, self.deltaT)

    #显示或隐藏光标
    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()


#保存曲线
def saveDrawing():
    turtle.hideturtle()
    #按时间生成文件名
    strdate = (datetime.now()).strftime("%Y%b%d %H%M%S")
    fileName = 'spiro-' + strdate
    print('保存的曲线名称:%s.eps/png' % fileName)
    #获取tkinter界面
    canvas = turtle.getcanvas()
    #将绘图保存为后记图像
    canvas.postscript(file = fileName + '.eps')
    #使用Pillow模式后记->PNG格式
    img = Image.open(fileName + '.eps')
    img.save('./' + fileName + '.png', 'png')
    #显示光标
    turtle.showturtle()


#流程
def main():
    #传入参数
    print('gennerating spirograph...')
    descStr="""This program draws Spirogaphs using Turtle module.
                这个程序使用Turtle模块绘制Spirogaphs
                When run with no arguments, this program draws random Spirographs.
                当没有参数运行时，这个程序会随机绘制螺旋图
                Terminology:
                术语:
                R:radius of outer circle
                R： 外圆半径
                r:radius of inner circle
                r： 内圆半径
                l: ratio of hole distance to r
                l： 孔距与r之比
                """
    parser = argparse.ArgumentParser(description=descStr)

    #添加预期参数
    parser.add_argument('--sparams', nargs=3, dest='sparams',required=False,
                        help='The three arguments in sparams:R, r, l')

    #
    args = parser.parse_args()

    #设置宽度为屏幕宽度的0.8
    turtle.setup(width=0.8)
    #设置光标形状
    turtle.shape('turtle')
    #设置标题
    turtle.title("螺旋图!")
    #添加键处理程序以保存我们的绘图
    turtle.onkey(saveDrawing, 's')
    #开始监听
    turtle.listen()

    #主光标隐藏
    turtle.hideturtle()

    #检查发送到--sparams的任何参数并绘制螺旋图
    if args.sparams:
        params = [float(x) for x in args.sparams]
        #用给定的参数绘制Spirograp
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        #创建动画对象
        spiroAnim = SpiroAnimator(4)
        #添加一个键处理程序来切换Turtle光标
        turtle.onkey(spiroAnim.toggleTurtles, 't')
        #添加关键点处理程序以重新启动动画
        turtle.onkey(spiroAnim.restart, 'space')
    #
    turtle.mainloop()

if __name__ == '__main__':
    main()