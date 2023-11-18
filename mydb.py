import mysql.connector

db = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    password = 'We79A7FcJPdnKb'
)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE mydb")

db.close()

