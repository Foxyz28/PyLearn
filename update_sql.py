# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
print('Open database successfully')

c.execute("UPDATE CAPACITANCE set DETAILURL = 'NO URL' where ID=1")
conn.commit()
conn.close()