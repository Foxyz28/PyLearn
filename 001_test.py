#coding:utf-8

from urllib import request

page = request.urlopen('https://www.digikey.com.cn/product-detail/zh/avx-corporation/C005YJR05PBSTR/478-7092-2-ND/3444124')
htmlcode = page.read()
htmlcodeSTR = htmlcode.decode('utf-8')

pageFile = open('pagecode.txt', 'w')
pageFile.write(htmlcodeSTR)
pageFile.close()


