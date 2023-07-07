import mysql.connector
db_connection = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "toor",
    database = "onlinedb2"
)
db_cursor = db_connection.cursor()
db_cursor.execute("alter table Students ADD hobby VARCHAR(20)")
db_cursor.execute("DESCRIBE Students")
for tb in db_cursor:
    print(tb)