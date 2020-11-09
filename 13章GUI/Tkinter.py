import tkinter as tk
import sys
# from tkinter import *
# 创建GUI
# widget = Label(None, text="This is my first Gui!!")
# widget.pack()
# widget.mainloop()

# # 创建GUI后在创建标签
# root = tk.Tk()
# widget = tk.Label(root)
# widget.config(text="My first GUI!!")
# widget.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
# root.mainloop()

# 创建GUI和一个Button按钮 退出窗口
# widget = tk.Button(None, text="Click Me", command=sys.exit)
# widget.pack()
# widget.mainloop()


# 创建GUI和Button按钮的操作事件
def result():
    print("The sum of 2+2 is ", 2+2)


# # 框架组件，可以组合小组件
# win = tk.Frame()
# win.pack()
# tk.Label(win, text="Click Add to get the sum or Quit to Exit").pack(side=tk.TOP)
# tk.Button(win, text="Add", command=result).pack(side=tk.LEFT)
# tk.Button(win, text="quit", command=win.quit).pack(side=tk.RIGHT)
# win.mainloop()

# 配置组件参数 如：字体大小颜色等
# root = tk.Tk()
# labelfont = ("time", 24, "italic")
# widget = tk.Label(root, text='Eat At JOES')
# widget.config(bg='black', fg='red')
# widget.pack(expand=tk.YES, fill=tk.BOTH)
# root.mainloop()

state = ''
buttons = []


def choose(i):
    global state
    state = i
    for btn in buttons:
        btn.deselect()
    buttons[i].select()


root = tk.Tk()
for i in range(4):
    radio = tk.Radiobutton(root, text=str(i), value=str(i), command=(lambda i=i: choose(i)))
    radio.pack(side=tk.BOTTOM)
    buttons.append(radio)
root.mainloop()
print("You chose the following number: ", state)
