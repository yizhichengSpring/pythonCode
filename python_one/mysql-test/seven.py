import pymysql

db = pymysql.connect('127.0.0.1','root','123456','test')

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("database version : %s" % data)

db.close()
#conn = pymysql.connect()


