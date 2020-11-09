import re
import urllib.request as request
from bs4 import BeautifulSoup
import requests


downLoadFile = 'F:\\小说'
shuhao = '61_61205'
start, end = 4523757, 4795158


def SetSrr(url):
    if (requests.get(url).status_code == 404):
        print("这是一个错误的网址")
        return []
    print("正在打开", url)

    l = []
    ''' 请求响应和不响应处理'''
    response = request.urlopen(url)

    html = response.read()
    soup = BeautifulSoup(html)
    item = soup.findAll('h1')
    title = re.match(r'(.*)<h1>(.*)</h1>(.*)', str(item), re.M | re.I).group(2)
    l.append(title.split(" ")[0])
    # l.append(title)
    strings = soup.findAll('div', id="content")[0]
    for string in strings:
        st = string.__str__()
        if (len(st.split('<br/>')) > 1):
            pass
        else:
            l.append(st)
    return l


# 串入字符串 写入文件；标题为l[0]
def SetDoc(l):
    if (len(l) < 2):
        return
    file_s = downLoadFile + l[0] + '.txt'
    file = open(file_s, 'w+', encoding='utf-8')
    for i in l:
        file.write('\t')
        for ii in i.split('  '):
            file.write(ii)
        file.write('\n')


# 开始自加数值；读取新文档；如果没有；跳过
def SetNum(num, n):
    l = [(num + i) for i in range(n)]
    sl = [str(l[i]) for i in range(len(l))]
    return sl


# ''' 自动产生新的url
# ''' 自己观察到：第一章的地址 https://www.biqudu.net/61_61205/4523757.html
# ''' 最后一张 https://www.biqudu.net/61_61205/4795158.html
def SetNewUrl(sl):
    urls = []
    for x in sl:
        xsr = 'https://www.biqudu.net/' + shuhao + '/' + x + '.html'
        urls.append(xsr)
    return urls


def SetTxts(urls):
    for url in urls:
        SetDoc(SetSrr(url))


print(
    '''
    --------------------------
    开始下载轮回乐园
    --------------------------
    ''')
SetTxts(SetNewUrl(SetNum(start, end)))
