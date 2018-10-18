#coding:utf-8

from urllib import request
import re


def get_html(url):
    reg = request.Request(url)
    reg.add_header("user-agent", "Mozilla/5.0")
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


print('请输入URL: ')
url = input()
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
