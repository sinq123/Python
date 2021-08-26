import urllib.parse as parse
from urllib.request import urlretrieve
import requests
from lxml import etree
import tkinter as TK
import json
import tkinter.ttk as ttk
import os
import time
import sys

music_info = []

# 判断文件夹是否存在， 不存在创建文件夹
def Exists(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    if not(os.path.exists(path)):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
    return

# 进度条
def Time_1():
    for i in range(1, 51):
        sys.stdout.write('\r')
        sys.stdout.write('{0}% |{1}'.format(int(i % 51) * 2, int(i % 51) * '■'))
        sys.stdout.flush()
        time.sleep(0.125)
    sys.stdout.write('\n')

# 清空列表
def delButton(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)


def GetList():
    delButton(text)
    music_info_List = []
    name = entry.get()
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    for x in range(10):
        params = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'new_json': '1',
            'remoteplace': 'txt.yqq.song',
            'searchid': '59272331134066183',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': str(x+1),
            'n': 10,
            'w': name,
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
            }
        response = requests.get(url, params=params)
        # 字符串转json格式
        music_josn = response.content.decode()
        # json格式转换为字典
        music_data = json.loads(music_josn)
        code = music_data['code']
        if code == 0:
            music_list = music_data['data']['song']['list']
            for music in music_list:
                music_name = music['name'] #歌曲名
                singer_name = music['singer'][0]['name']#歌手
                str_3='''https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"1825194589","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'''
                singer_url = str_3 % (music['mid']) # 歌曲地址
                music_info_List.append((music_name, singer_name, singer_url))
            music_info = music_info_List
            i = 0
    if len(music_info_List) > 0:
        i = 0
        for Text in music_info_List:
            i = i + 1
            text.insert("", TK.END, values=(i, Text[1], Text[0], Text[2]))
            text.update()
    else:
        return False
    return True


def DownloadMusic():
    try:
        #列表框控件
        # 获取选中列表的代号 元组形式显示
        #i = text.curselection()
        #Getli = text.get(i[0])
        #print(type(Getli))

        # 获取选中列表的代号 字典形式显示
        curItem = text.item(text.focus())
        # 获取播放地址，歌名，str形式显示
        url = curItem["values"][3]
        musicName = curItem["values"][2]
        musicSige= curItem["values"][1]
        # 组合下载地址
        content_json=requests.get(url)
        dict_2=json.loads(content_json.text)
        url_ip=dict_2['req']['data']['freeflowsip'][1]
        purl=dict_2['req_0']['data']['midurlinfo'][0]['purl']
        downlad=url_ip+purl
        # 创建文件夹
        music_path = "%s\\音乐文件夹\\" % (os.path.dirname(os.path.realpath(__file__)))
        # 判断文件夹是否存在
        Exists(music_path)
        # 以下简单操作，不保证一定成功，以上是保证一定成功
        #os.mkdir('./QQ音乐')
        #保存路径
        music_path = music_path + musicName + "_"+ musicSige + '.mp3'
        #下载保存
        urlretrieve(url=downlad,filename=music_path)
        Time_1()
        print('{}.mp3下载完成！'.format(musicName))
    except Exception as e:
        print(e)
        print('下载失败')

    return


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
#text = TK.Listbox(frame_2, font=('微软雅黑', 25), width='27', height='6')
# 列表（树结构）
#show = "tree", 第一列也会被显示出来
#也可用show = "headings" 把第一列隐藏起来
#height 的单位是字符，本例里可以显示10行
text = ttk.Treeview(frame_2, show="headings", height=10, columns=("a", "b", "c", "d", "e"))
# 表格的标题
#指定第一列的宽度和名称， 如果show = "headings", 这一列就被隐藏。
text.column("a", width=40, anchor="center")
text.column("b", width=150, anchor="center")
text.column("c", width=250, anchor="center")
text.column("d", width=350, anchor="center")
text.column("e", width=0, anchor="center")
text.heading("a", text="编号")
text.heading("b", text="歌手")
text.heading("c", text="歌曲")
text.heading("d", text="播放地址")
text.heading("e", text="")

# 按钮控件
button = TK.Button(frame_3, text="开始下载", font=('微软雅黑', 18), fg='Purple', width=10, height=1, command=lambda : DownloadMusic())
button1 = TK.Button(frame_3, text="退出", font=('微软雅黑', 18), fg='Purple', width=10, height=1, command=root.quit)
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
