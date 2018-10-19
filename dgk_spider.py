# -*- coding: utf-8 -*-

import requests
import os
from lxml import html


# header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                         "Chrome/57.0.2987.98 Safari/537.36 LBBROWSER "}


header = {}


# print('请输入URL: ')
# url = input()
url = 'https://www.digikey.com.cn/product-detail/zh/kemet/C0402C220K5GACTU/399-7775-2-ND/2196444'    # 设置 url
if url:    # 判断 url 是否合法
    pass
else:
    url = '__defaulturl__'


def get_html(url):    # 抓取 url 内的信息
    reg = requests.get(url, headers=header)    # 加入 headers
    page = reg.content
    # finalpage = html.fromstring(page)    # 将 string 转为 element 对象, 方便 xpath 处理
    return page


def get_dgkID(text):    # 获取 text 内的 dgkID
    page = html.fromstring(text)  # 将 string 转为 element 对象, 方便 xpath 处理
    dgkid = page.xpath('//*[@id="PartNumber"]')
    n = 1
    for dgkidprint in dgkid:
        print('No. %s' % n, ':', dgkidprint)
        n = n + 1


def save_html(html, filename='temp.html', path='download'):    # 将读取到的 html 写入文件
    filepath = os.path.join(path, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        print('output file path = ', filepath)
        f.write(html)


pp = get_html(url)
get_dgkID(pp)
# save_html(pp)


# pageFile = open('pagecode.txt', 'w', encoding='utf-8')
# pageFile.write(htmlcode)
# pageFile.close()
