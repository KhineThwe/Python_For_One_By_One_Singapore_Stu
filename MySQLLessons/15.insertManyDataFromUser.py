import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "toor",
    database="onlinedb2"
)

dataType = "INSERT INTO students(id,name,age,attend,hobby) VALUES(%s,%s,%s,%s,%s)"

num_data_sets = int(input("Enter the number of data sets you want to insert: "))

data = []
for _ in range(num_data_sets):
    student_id = int(input("Enter student id: "))
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))
    student_attendance = int(input("Enter student attendance: "))
    student_hobby = input("Enter student hobby: ")

    data.append((student_id,student_name,student_age,student_attendance,student_hobby))

db_cursor = db_connection.cursor()

db_cursor.executemany(dataType,data)

db_connection.commit()

print("Data are inserted")
print(db_cursor.rowcount)

db_cursor.execute("SELECT * From students")
for db in db_cursor:
    print(db)

db_connection.close()