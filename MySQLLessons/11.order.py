import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)
dbCursor = db_connection.cursor()
dbCursor.execute("Select id,name,age From students ORDER By age DESC")
data = dbCursor.fetchall()
for db in data:
    print("%d %s %d"%(db[0],db[1],db[2]))