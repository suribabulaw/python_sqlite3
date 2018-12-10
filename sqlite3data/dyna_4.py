import sqlite3 as sql_room
conTodb = sql_room.connect('dyna.db')
db_cursor = conTodb.cursor()
print('press 1 to create a table')
print('press 2 to inset data in2 table')
print('press 3 read data from table')
print('press 4 read one data')
print('press 5 delete data')
print('press 6 to  update data')
print('')
option = int(input('enter ur namber'))

if option == 1 :
    stud = input('enter table')
    db_cursor.execute("create table if not exists  "+ stud+" (idno integer  PRIMARY KEY,name text , marks integer ,gred real )")
    print('create data base')
if option == 2 :
    indo = int(input('enter id '))
    name = input('enter name')
    marks = int(input('enter maks'))
    gret = float(input('enter grede'))
    db_cursor.execute('insert into student values(?,?,?,?)',(indo,name,marks,gret))
    conTodb.commit()
    print('inseted  data in table ')
if option == 3:

    db_cursor.execute('select * from student')
    result= db_cursor.fetchall()
    #print(result)
    for x in result:
        print(x)
    #print(' data read all base')
if option == 4 :
    id = int(input('enter id which u whant ti desplay'))
    db_cursor.execute('select * from student where (?)',(id,))
    result = db_cursor.fetchone()
    for x in result :
        print(x)
    print( id ,'read one value only')

if option == 5:
    id = int(input('enter id which u whant to delete'))
    db_cursor.execute('delete from student where (?)',(id,))
    conTodb.commit()
    print(id , 'delete data from table value only')
if option >= 6 :
    id = int(input('enter id which want chenge id '))
    name1 = input('enter name u what to chenge')
    fee = input('feee')
    db_cursor.execute('update student set  gred= ? ,name=? where idno=?',(fee,name1 ,id,))
    conTodb.commit()
    #print( option ,' is not a vaild please selete vaild nbr onluy')
if option >= 7 :
    print( option ,' is not a vaild please selete vaild nbr onluy')

print('than you')


