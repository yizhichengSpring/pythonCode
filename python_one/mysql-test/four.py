import sqlite3

conn = sqlite3.connect('mrsoft.db')

cursor = conn.cursor()

cursor.execute('UPDATE user SET name = ? where id = ? ',('易志成',1))

cursor.execute('SELECT * FROM user')

result1=cursor.fetchall()

print(result1)

cursor.close()

conn.commit()

conn.close()