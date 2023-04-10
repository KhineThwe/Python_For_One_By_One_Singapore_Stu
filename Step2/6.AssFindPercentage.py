if __name__ == '__main__':
    n = int(input("Enter number of students"))#4
    students_marks = {}
    result = []
    for i in range(n):
        #two ways #one way#limitation
        name,mark1,mark2,mark3 = input("Username : eg: 20 30 40").split()#Khine 20 30 40
        mark = (mark1,mark2,mark3)
        scores = list(map(float,mark))#[20.0,30.0,40.0]
        print(scores)
        students_marks[name] = scores#{"Khine":[20.0,30.0,40.0],"Zar":[20.0,30.0,40.0]}
    print(students_marks)




