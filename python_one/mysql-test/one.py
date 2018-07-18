import sqlite3

#连接到SQLite数据库
#数据库文件是mrsoft.db 如果不存在，则创建一个
conn = sqlite3.connect('mrsoft.db')
#创建一个Cursor
cursor = conn.cursor()
#执行一条sql
cursor.execute('create  table  user(id int(10) primary key ,name varchar(20))')
#关闭游标
cursor.close()
#关闭connection
conn.close()