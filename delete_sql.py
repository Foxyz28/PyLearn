# -*- coding: utf-8 -*-


import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
print('Open database successfully')

c.execute("DELETE from CAPACITANCE where ID=1")
conn.commit()
conn.close()