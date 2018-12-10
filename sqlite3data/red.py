import sqlite3 as sql
connt = sql.connect('suri.db')
cur = connt.cursor()
cur.execute('select * from employee')
result = cur.fetchall()
print(result)
