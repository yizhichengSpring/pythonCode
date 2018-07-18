import sqlite3

conn=sqlite3.connect('mrsoft.db')

cursor=conn.cursor()

cursor.execute('delete  from  user where  id = ?',(1,))

cursor.execute('select * from user')


result1 = cursor.fetchall()

print(result1,type(result1))

cursor.close()

conn.commit()


conn.close()