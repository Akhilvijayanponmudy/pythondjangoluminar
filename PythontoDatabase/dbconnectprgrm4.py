import mysql.connector

db=mysql.connector.connect(

    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database="pythondecember"
)
try:
    cursor=db.cursor()
    sql="insert into movie values(100,'pirates','2004',4)"
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()

db.close()
