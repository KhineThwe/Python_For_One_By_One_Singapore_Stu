import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)

dataType = "INSERT INTO Students(id,name,age,attend,hobby) values(%s,%s,%s,%s,%s)"
data = (102,"NT",101,4,"Research")

db_cursor = db_connection.cursor()
db_cursor.execute(dataType,data)

db_connection.commit()
print("Datas are inserted")
print(db_cursor.rowcount)

db_cursor.execute("SELECT * FROM Students")
for tb in db_cursor:
    print(tb)