# 不能使用
from urllib import parse
import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re


class APP:

    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = "VIP视频破解"
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        group = tk.Label(frame_1, text="暂时只有一个视频播放通道：", padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text="唯一通道", variable=self.v, value=1, width=10, height=3)
        lable = tk.Label(frame_2, text="请输入视频连接：")

        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor="Fuchsia", highlightthickness=1, width=35)
        play = tk.Button(frame_2, text="播放", font=("宋体", 12), fg="Purple", width=2, height=1, command=self.video_play)

        frame_1.pack()
        frame_2.pack()

        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        lable.grid(row=0, column=0)
        entry.grid(row=0, column=1)

        play.grid(row=1, column=3, ipadx=10, ipady=10)

    def video_play(self):

        port = "https://jx.idc126.net/jx/?url="

        if re.match(r"^https?:/{2}\w.+$", self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            webbrowser.open(port + ip)
        else:
            ip = "视频链接地址无效，请重新输入！"
            ip += self.url.get()
            msgbox.showerror(title="错误", message=ip)

    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.loop()


