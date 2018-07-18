import pymysql


db = pymysql.connect('127.0.0.1','root','123456','test')

cursor = db.cursor()

cursor.execute("select * from books")

result=cursor.fetchall()

print(result)

db.close()

