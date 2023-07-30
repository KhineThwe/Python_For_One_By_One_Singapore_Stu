import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)
dbCursor = db_connection.cursor()
dbCursor.execute("SELECT id,name,age FROM students")
data = dbCursor.fetchone()
print(data)