import sqlite3 as sql
connect_got = sql.connect('suri.db')
print('db created')
cur=connect_got.cursor()
cur.execute("create table Employee(id integer ,name substring ,salary real )")
print('table creacted')
