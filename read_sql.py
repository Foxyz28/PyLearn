# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
print('Open database successfully')

cursor = c.execute("SELECT * from CAPACITANCE")
for raw in cursor:
    print('ID: ', raw[0])
    print('URL: ', raw[1])
    print('productID: ', raw[2])
    print('vendor-ID: ', raw[3])
    print('Qty. : ', raw[4])
    print('\n')

print('Operation done successfully')
conn.close()