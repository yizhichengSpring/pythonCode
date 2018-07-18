import pymysql

db = pymysql.connect('47.95.3.32','root','123456','test')

cursor = db.cursor()

data = [('python1','Python','79.70','2018-05-20'),('python2','Python','79.80','2018-05-20')]


cursor.executemany("INSERT INTO books(name,category,price,publish_time) values (%s,%s,%s,%s)",data)

db.commit()

db.close()