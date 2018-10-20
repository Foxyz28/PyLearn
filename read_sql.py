# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
print('Open database successfully')

n = 2

cursor = c.execute("SELECT * from CAPACITANCE")
for raw in cursor:
    print('ID: ', raw[0])
    print('URL: ', raw[1])
    print('德捷电子 零件编号：', raw[2])
    print('制造厂商 零件编号：', raw[3])
    print('值：', raw[4])
    print('误差：', raw[5])
    print('电压：', raw[6])
    print('工作温度：', raw[7])
    print('尺寸：', raw[8])
    print('数量：', raw[9])
    print('\n')

print('Operation done successfully')
conn.close()