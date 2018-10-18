#coding:utf-8

from urllib import request
import re


def get_html(url):
    page = request.urlopen(url)
    html = page.read()
    htmlSTR = html.decode('utf-8')
    return htmlSTR


def get_img(html):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)
    imglist = reg_img.findall(html)
    x = 0
    for img in imglist:
        print(img)
        request.urlretrieve(img, '%s.jpg' % x)
        x = x + 1
    return


print('请输入URL: ')
url = input()
if url:
    pass
else:
    url = '__defaulturl__'

get_img(get_html(url))

# pageFile = open('pagecode.txt', 'w', encoding='utf-8')
# pageFile.write(htmlcode)
# pageFile.close()
