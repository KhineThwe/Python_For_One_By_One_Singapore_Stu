import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)

dbCursor = db_connection.cursor()
dbCursor.execute("DELETE FROM students where id = 103")
db_connection.commit()
dbCursor.execute("SELECT id,name,age FROM students")
for db in dbCursor:
    print("%d %s %d"%(db[0],db[1],db[2]))