
import requests
from datetime import datetime
import re
#import json
import time
import os

url = "http://xxxxxxxx/api/?d=pc&c=video&"
m3u8_url ='https://xxxxxxxxxxxxxxx/videos/cherry-prod/2020/03/01/2dda82de-5b31-11ea-b5ae-1c1b0da2bc3f/hls/480/'
header = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"}
vediomassag=''
TimeStamp = int(datetime.timestamp(datetime.now()))

#自定义函数获取分类
def get_vediocategory(url, TimeStamp):
    cgURL = url + "m=categories&timestamp=" + str(TimeStamp) + '&'
    response = requests.get(cgURL, headers=header)
    category = response.text
    # strrr='"%s"'%category
    # return strrr
    return category

#获取分类后的视频列表
def get_vedioList(url, TimeStamp, tagID):
    listURL = url + "m=lists&timestamp=" + str(TimeStamp) + '&' + "page=1&tag_id=" + str(tagID) + "&sort_type=&is_vip=0"
    response = requests.get(listURL, headers=header)
    vedioLists = response.text
    return vedioLists

#获取单个视频的详细信息
def get_vediomassages(url, TimeStamp, vedioID):
    videoURL = url + "m=detail&timestamp=" + str(TimeStamp) + '&' + "&id=" + str(vedioID)
    response = requests.get(videoURL, headers=header)
    vediomassag = response.text
    return vediomassag

#将下载的m3u8文件放进创建的ts列表文件中
def get_m3u8List(m3u8_url,vediomassag):
    lasturl = r'"m3u8_720_url":"(.*?)","download_url'
    last_url =re.findall(lasturl,vediomassag)
    lastURL=m3u8_url+str(last_url)
    response = requests.get(lastURL, headers=header)
    tsList = response.text
    cur_path='E:\\files' #在指定路径建立文件夹
    try:
        if not os.path.isdir(cur_path): #确认文件夹是否存在
            os.makedirs(cur_path) #不存在则新建
    except:
        print("文件夹存在")
    filename=cur_path+'\\t2.txt' #在文件夹中存放txt文件
    f = open(filename,'a', encoding="utf-8")
    f.write(tsList)
    f.close
    print('创建%s文件成功'%(filename))
    return filename

# 提取ts列表文件的内容，逐个拼接ts的url，形成list
def get_tsList(filename):
    ls = []
    with open(filename, "r") as file:
        line = f.readlines()
        for line in lines:
            if line.endswith(".ts\n"):
                ls.append(line[:-1])
    return ls

# 批量下载ts文件
def DownloadTs(ls):
    length = len(ls)
    root='E:\\mp4'
    try:
        if not os.path.exists(root):
            os.mkdir(root)
    except:
        print("文件夹创建失败")
    try:
        for i in range(length):
            tsname = ls[i][:-3]
            ts_URL=url+ls[i]
            print(ts_URL)
            r = requests.get(ts_URL)
            with open(root, 'a') as f:
                f.write(r.content)
                f.close()
                print('\r' + tsname + " -->OK ({}/{}){:.2f}%".format(i, length, i * 100 / length), end='')
                print("下载完毕")
    except:
        print("下载失败")

'''# 整合所有ts文件，保存为mp4格式（此处函数复制而来未做实验，本人直接在根目录
命令行输入copy/b*.ts 文件名.mp4,意思是将所有ts文件合并转换成自己命名的MP4格式
文件。）
def MergeMp4():
    print("开始合并")
    path = "E://mp4//"
    outdir = "output"
    os.chdir(root)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
        os.system("copy /b *.ts new.mp4")
        os.system("move new.mp4 {}".format(outdir))
    print("结束合并")'''

if __name__ == '__main__':
    # 将获取的分类信息解码显示出来
    # print(json.loads(get_vediocategory(url, TimeStamp)))
    print(get_vediocategory(url, TimeStamp))
    tagID = input("请输入分类对应的id")
    print(get_vedioList(url, TimeStamp, tagID))
    vedioID = input("请输入视频对应的id")
    get_vediomassages(url, TimeStamp, vedioID)
    get_m3u8List(m3u8_url,vediomassag)
    get_tsList(filename)
    DownloadTs(ls)
    # MergeMp4()