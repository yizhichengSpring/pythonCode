import sqlite3

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()


cursor.execute('insert  into user(id,name) values ("1","zs")')
cursor.execute('insert  into user(id,name) values ("3","ls")')
cursor.execute('insert  into user(id,name) values ("4","ww")')

cursor.close()

conn.commit()


conn.close()

