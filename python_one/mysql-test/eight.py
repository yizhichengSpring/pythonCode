import pymysql

db = pymysql.connect('47.95.3.32','root','123456','test')

cursor=db.cursor()

cursor.execute("DROP TABLE IF EXISTS books")

sql = """
    
    create table books (
    
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) DEFAULT NULL,
    publish_time date DEFAULT NULL,
    PRIMARY KEY (id)
    
    ) ENGINE =MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET = utf8;


"""
cursor.execute(sql)

db.close()