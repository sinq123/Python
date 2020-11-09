import requests
from lxml import etree
import tkinter as TK
import json

music_info = []


def GetList():
    music_info_List = []
    name = entry.get()
    # name = name.encode("utf-8")
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=58519642427860901&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w='
    url = url + str(name)
    url = url + '&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    response = requests.get(url)
    # 字符串转json格式
    music_josn = response.content.decode()
    # json格式转换为字典
    music_data = json.loads(music_josn)
    code = music_data['code']
    if code == 0:
        music_list = music_data['data']['song']['list']
        for music in music_list:
            music_name = music['name']
            singer_name = music['singer'][0]['name']
            music_info_List.append((music_name, singer_name))
        music_info = music_info_List
        if len(music_info) > 0:
            for Text in music_info:
                text.insert(TK.END, '歌曲:%s 歌手:%s' % (Text[0], Text[1]))
                text.see(TK.END)
                text.update()
        return True
    else:
        return False


# 1.创建窗口
root = TK.Tk()
# 2.窗口标题
root.title('QQ音乐下载')
# 3.窗口大小及显示位置， 中间是小写是x
root.geometry('550x400+550+230')
# 禁止修改窗口大小
root.resizable(False, False)
frame_1 = TK.Frame(root)
frame_2 = TK.Frame(root)
frame_3 = TK.Frame(root)
# 4.标签控件
label = TK.Label(frame_1, text='请输入需要下载的歌曲或歌手', font=('微软雅黑', 10))
# 输入控件()
entry = TK.Entry(frame_1, font=('微软雅黑', 25), width='15')
root.bind('<Return>', (lambda event, e=entry: GetList()))
# 列表框控件
text = TK.Listbox(frame_2, font=('微软雅黑', 25), width='27', height='6')
# 按钮控件
button = TK.Button(frame_3, text="开始下载", font=('微软雅黑', 18), fg='Purple', width=10, height=1)
button1 = TK.Button(frame_3, text="退出", font=('微软雅黑', 18), fg='Purple', width=10, height=1)
# 控件布局
frame_1.pack()
frame_2.pack()
frame_3.pack(side='right')
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
text.grid(row=1, columnspan=2)
button.grid(row=2, column=0)
button1.grid(row=2, column=1)
root.mainloop()
