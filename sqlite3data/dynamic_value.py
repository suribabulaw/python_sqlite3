
id = int(input('id enter'))
name = input('name')
salary = input('salary')
import sqlite3 as sql
conn = sql.connect('suri.db')
cur=conn.cursor()
cur.execute('insert into employee values (?,?,?)',(id,name,salary))
conn.commit()