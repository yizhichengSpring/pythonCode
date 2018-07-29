import pymysql
import requestsdemo
#
# db = pymysql.connect('47.95.3.32','root','123456','test')
#
# cursor = db.cursor()
#
# cursor.execute("select * from books")
#
# result=cursor.fetchall()
#
# print(result)
#
# db.close()
#


db = pymysql.connect('47.95.3.32','root','123456','test')

cursor = db.cursor()

cursor.execute("select * from books")

result=cursor.fetchall()

print(result,type(result))

db.close()