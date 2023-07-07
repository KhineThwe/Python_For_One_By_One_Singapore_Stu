import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)
dataType = "INSERT INTO Students(id,name,age,attend,hobby) values(%s,%s,%s,%s,%s)"
data = [(103,"ST",1000,4,"Travelling"),(104,"WT",1010,4,"Reading")]

db_cursor = db_connection.cursor()
db_cursor.executemany(dataType,data)

db_connection.commit()
print("Datas are inserted")
print(db_cursor.rowcount)

db_cursor.execute("SELECT * FROM Students")
for tb in db_cursor:
    print(tb)