import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)
dbCursor = db_connection.cursor()
# dbCursor.execute("CREATE TABLE cost(id int primary key AUTO_INCREMENT,monthly int,totalCost int)")
#
# dataType = "INSERT INTO cost(id,monthly,totalCost) values(%s,%s,%s)"
# data = [(102,150,1500),(104,100,1200),(4,250,2500)]
#
# dbCursor.executemany(dataType,data)
# db_connection.commit()
# print("Datas are inserted!")

dbCursor.execute("SELECT students.id,students.name,students.age,cost.id,cost.totalCost,cost.monthly FROM cost "
                 "join students on cost.id = students.id")
data = dbCursor.fetchall()
print("id  name  age  CostID  TotalCost  Monthly")
for db in data:
    print("%d %s %d %d %d %d"%(db[0],db[1],db[2],db[3],db[4],db[5]))