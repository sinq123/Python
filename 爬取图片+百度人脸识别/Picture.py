from bs4 import BeautifulSoup
import requests
import os
import time
from selenium import webdriver


save_path = 'F://Pictrue/'
url_path = 'https://www.pexels.com/search/'
headers = {
    'Referer': 'https://www.pexels.com/',
    'Upgrade-Insecure-Requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
searchWord = 'beauty'
urls = [url_path+searchWord+'/?page={}'.format(str(i)) for i in range(1, 100)]

if not os.path.exists(save_path):
    os.mkdir(save_path)
page = 1
for url in urls:
    img_list = []
    # wb_data = requests.get(url=url, headers=headers)
    driver = webdriver.Chrome()
    driver.get(url)
    print("当前爬取页面链接", url)
    wb_data = driver.page_source
    driver.quit()
    soup = BeautifulSoup(wb_data, 'lxml')
    imgs = soup.select('article > a > img')
    for img in imgs:
        photo_src = img.get('src')
        img_list.append(photo_src)
        print("第{}页, 共计{}张图片".format(page, len(img_list)))
    for item in img_list:
        data = requests.get(url=item, headers=headers)
        fp = open(save_path + item.split('?')[0][-10:], 'wb')
        fp.write(data.content)
        fp.close()
        print("第{}图片下载完成".format(int(page)))
        page = page + 1
        time.sleep(2)
