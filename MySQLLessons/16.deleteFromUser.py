import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)

db_cursor  = db_connection.cursor()

student_id_to_delete = input("Enter the ID of the student you want to delete: ")

delete_query = "DELETE FROM students WHERE id=%s"
db_cursor.execute(delete_query,(student_id_to_delete,))

#execute() --> parameters should be list,tuple,dictionary

db_connection.commit()

select_id = input("Enter the id of the students you want to select: ")
select_query = "SELECT id,name,age FROM students WHERE id=%s"
db_cursor.execute(select_query,(select_id,))

for db in db_cursor:
    print("%d %s %d"%(db[0],db[1],db[2]))

db_connection.close()