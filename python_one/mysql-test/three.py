import sqlite3

conn = sqlite3.connect('mrsoft.db')

cursor = conn.cursor()

cursor.execute('select * from user where id> ?',(2,))


#result1 = cursor.fetchone()
#result2 = cursor.fetchmany(3)
result3 = cursor.fetchall()
print(result3)


cursor.close()


conn.close()