import mysql.connector

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "toor",
    database = "onlineDB2"
)
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE Students(id int primary key AUTO_INCREMENT,"
                  "name VARCHAR(30),age SMALLINT,attend TINYINT)")
db_cursor.execute("DESCRIBE Students")
for tb in db_cursor:
    print(tb)