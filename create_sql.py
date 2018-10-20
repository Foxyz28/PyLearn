# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect('test.db')
print('Open database successfully')
c = conn.cursor()
c.execute('''CREATE TABLE CAPACITANCE(
ID            INT PRIMARY KEY NOT NULL,
DETAILURL     TEXT,
PRODUCTID     TEXT,
VENDORID      TEXT,
PRODUCTVALUE  TEXT,
TOLERANCE     TEXT,
VOLTAGE       TEXT,
WORKTEMP      TEXT,
MOLDSIZE      TEXT,
QTYAVAILABLE  INT);''')
print('Table created successfully')
conn.commit()
conn.close()
