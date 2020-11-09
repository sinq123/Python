import requests
import time
import os
from lxml import etree


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


url = "https://www.mzitu.com/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Referer': 'https://www.mzitu.com/'

}

response = requests.get(url=url, headers=headers)

# 网页返回代号 200成功
# print(response.status_code)

if response.status_code == 200:
    html = response.text
    content = etree.HTML(html)
    # 获取图片链接列表
    url_list = content.xpath('//*[@id="pins"]/li/a/@href')
    # 打印图片链接列表
    # print(url_list)

    # 历遍图片链接
    for url in url_list:
        i = 1
        while i < 100:
            # 没有时 抛出异常返回继续下一个链接
            try:
                response_jpg = requests.get(url=url, headers=headers).text
                content_jpg = etree.HTML(response_jpg)
                # 图片位置 /html/body/div[2]/div[1]/div[3]/p/a/img
                img = content_jpg.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0]
                # 图片名称 html/body/div[2]/div[1]/div[3]/p/a/img
                name = content_jpg.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@alt')[0]
                # 下一页 /html/body/div[2]/div[1]/div[4]/a
                url = content_jpg.xpath('/html/body/div[2]/div[1]/div[4]/a[last()]/@href')[0]
                # 保存
                # 获取文件的绝对路径+images文件
                path = "%s\\images\\" % (os.path.dirname(os.path.realpath(__file__)))
                # 判断文件夹是否存在
                Exists(path)
                req = requests.get(url=img, headers=headers).content
                with open(f'{path}{name}_{i}.jpg', 'wb') as f:
                    f.write(req)
                    print(f'{path}{name}_{i}.jpg', '爬取完成！')
                i += 1
            except IndexError:
                break
        # 暂停500ms
        time.sleep(0.5)
else:
    Error = "错误代码%d," % (response.status_code)
    print(Error)
