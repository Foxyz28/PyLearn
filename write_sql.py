# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
print('Open database successfully')

c.execute("INSERT INTO CAPACITANCE (ID,DETAILURL,PRODUCTID,VENDORID,QTYAVAILABLE) VALUES (2, 'https://www.digikey.com.cn', '399-14264-2-ND', 'C0201C1', 105000)")

conn.commit()
print('Records created successfully')
conn.close()
