# -*- coding: utf-8 -*-

import requests
import os
import time
from lxml import html


cookie = 'WC_SESSION_ESTABLISHED=true; WC_AUTHENTICATION_-1002=%2d1002%2cxClFneevJTCQwIkhZMqB6nffX7k%3d; ' \
         'WC_ACTIVEPOINTER=%2d7%2c10001; _ga=GA1.3.1188687891.1539854225; _gid=GA1.3.1764178619.1539854225; ' \
         '_msuuid_6fzke3kdm0=1F7D86DB-9B96-46E0-8AE5-47F774F68767; ' \
         'WC_PERSISTENT=GEe3ZVXGgR%2f3m%2bZs1753xkDxZLM%3d%0a%3b2018%2d10%2d18+04%3a17%3a05%2e514%5f1539854225509' \
         '%2d31121%5f10001%5f%2d1002%2c%2d7%2cCNY%5f10001; ' \
         'WC_USERACTIVITY_-1002=%2d1002%2c10001%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cnull%2cuGrL3%2fz' \
         '%2bLA6Cj2UpqYs7GTu4hXweHTv4JGiLQRB%2bvVrwuriPkes%2bG0mMa9ATRkj7LFHFalwsKi7m' \
         '%0a7EN2Fup29r4pB0SkICZ8CXOhH33JCNY%2fyG6yJPpDwSaPR18%2bT%2f4dCuoI1%2fYxbYAgyY0Y2Ocu7A%3d%3d; ' \
         'WC_GENERIC_ACTIVITYDATA=[1275063868%3atrue%3afalse%3a0%3avMWqKbb66bBjytGAY4XLwHwWAXI%3d][' \
         'com.ibm.commerce.context.audit.AuditContext|1539854225509%2d31121][' \
         'com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][' \
         'com.digikey.commerce.context.UserContext|null][CTXSETNAME|Store][' \
         'com.ibm.commerce.context.globalization.GlobalizationContext|%2d7%26CNY%26%2d7%26CNY][' \
         'com.ibm.commerce.catalog.businesscontext.CatalogContext|10001%26null%26false%26false%26false][' \
         'com.ibm.commerce.context.base.BaseContext|10001%26%2d1002%26%2d1002%26%2d1][' \
         'com.ibm.commerce.context.experiment.ExperimentContext|null][' \
         'com.ibm.commerce.context.entitlement.EntitlementContext|10001%2610001%26null%26%2d2000%26null%26null%26null' \
         '][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null]; rvps=2196444; ' \
         'i10c_focloir=10:e2ee1852bd4d8fd64a61a3867e7820e3:0:05e06fedd0e5f6473d1c9860a867f2f0; ' \
         'i10c_focloir_data=579:10:e2ee1852bd4d8fd64a61a3867e7820e3:0:05e06fedd0e5f6473d1c9860a867f2f0; ' \
         'JSESSIONID=0001c_vRpDEnqD4BZjcX_HXsG-r:-OHDDV; ' \
         'TS01b442d5' \
         '=01460246b6ea2cb5aa70fe7a6529b25691a5e0d5d8227f643ffc356d8dfa0fa3322da36e6e02b10d797145d8d8e30facfde03e1999' \
         '; utag_main=v_id:01668676cbbe0068720398188c6003073001b06b00978$_sn:4$_ss:0$_st:1539931895254$ses_id' \
         ':1539930073693%3Bexp-session$_pn:2%3Bexp-session; ' \
         '__CT_Data=gpv=15&ckp=tld&dm=digikey.com.cn&apv_53471_www=30&cpv_53471_www=15 '


header = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.100 Safari/537.36 ',
    'Referer': 'https://www.digikey.com.cn/product-detail/zh/kemet/C0402C220K5GACTU/399-7775-2-ND/2196444'
}


# header = {}


# print('请输入URL: ')
# url = input()

#  设置url
'''
if url:    # 判断 url 是否合法
    pass
else:
    url = '__defaulturl__'
'''


def get_html(inputurl):    # 抓取 url 内的信息
    reg = requests.get(inputurl, headers=header)    # 加入 headers 抓取信息
    page = reg.content    # 获取内容
    # finalpage = html.fromstring(page)    # 将 string 转为 element 对象, 方便 xpath 处理
    return page


def get_maininfo(text):    # 获取 text 内的 dgkID
    page = html.fromstring(text)  # 将 string 转为 element 对象, 方便 xpath 处理
    n = 1
    while n <= 25:
        productID = page.xpath('//*[@id="accordionNav"]/tr[%d]/td[4]/a/text()' % n)    # 提取 productID
        #  tr[4] ~ tr[28]
        a = len(productID)
        # print(a)
        for productIDp in productID:
            print(productIDp)
        n = n + 1


def save_html(html, filename='main0201.html', path='download'):    # 将读取到的 html 写入文件
    filepath = os.path.join(path, filename)
    with open(filepath, 'wb') as f:
        print('output file path = ', filepath)
        f.write(html)


maxpage = 10
pagenum = 1
while pagenum <= maxpage:
    urlbf = 'https://www.digikey.com.cn/products/zh/电容器/陶瓷电容器/60?formName=KeywordSearchForm&pageNumber='
    urlaf = '&sort=&sortDescending=&sortType=&qtyRequested=&c=60&keywords=&rfUofM=&PV=17210%7C4279783534%7C安装类型&PV' \
            '=17169%7C4279742636%7C封装%2F外壳&PV=18753%7C4279795329%7C零件状态&auto=false '
    urlnum = '%d' % pagenum
    url = urlbf + urlnum + urlaf
    # print(url)
    print('第%d页' % pagenum)
    page = get_html(url)
    get_maininfo(page)
    time.sleep(1)
    pagenum = pagenum + 1

# pp = get_html(url)
# get_maininfo(pp)
# save_html(pp)
