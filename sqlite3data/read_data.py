import sqlite3 as sql
conn = sql.connect('suri.db')
print('database connected to suri.db')
cur = conn.cursor()
cur.execute("insert into employee values(101,'suri',1200000)")
conn.commit()
print('DATA INSERTED INTO SURI.DB')
conn.close()





