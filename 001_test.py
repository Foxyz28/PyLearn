#coding:utf-8

from urllib import request
import re


def get_html(url):
    reg = request.Request(url)
    reg.add_header("user-agent", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11")
    page = request.urlopen(reg)
    html = page.read()
    htmlstr = html.decode('utf-8')
    return htmlstr


def get_dgkID(html):
    reg = r'content="sku:\d{3}\-\d{4}\-\d\-\w{2}"'
    reg_dgkid = re.compile(reg)
    dgkidlist = reg_dgkid.findall(html)
    x = 0
    for dgkid in dgkidlist:
        print(dgkid)
    return


def save_html(html):
    pagefile = open('pageFile.html', 'w', encoding='utf-8')
    pagefile.write(html)
    pagefile.close()
    return


# print('请输入URL: ')
# url = input()
url = 'https://www.digikey.com.cn/product-detail/zh/kemet/C0402C220K5GACTU/399-7775-2-ND/2196444'
if url:
    pass
else:
    url = '__defaulturl__'


pp = get_html(url)
get_dgkID(pp)
save_html(pp)


# pageFile = open('pagecode.txt', 'w', encoding='utf-8')
# pageFile.write(htmlcode)
# pageFile.close()
