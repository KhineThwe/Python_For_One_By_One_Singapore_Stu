from Student import *
if __name__ == '__main__':
    student = Student()
    rollNo,name = student.getStudentInfo()
    print("Roll No: ",rollNo)
    print("Name: ",name)