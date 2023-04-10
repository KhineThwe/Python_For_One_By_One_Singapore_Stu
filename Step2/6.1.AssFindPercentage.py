if __name__ == '__main__':
    n = int(input("Enter number of students"))#4
    students_marks = {}
    result = []
    for i in range(n):
        #new way#arbitrary
        name,*mark = input("Username : eg: 20 30 40").split()#Khine 20 30 40
        scores = list(map(float,mark))#[20.0,30.0,40.0]
        print(scores)
        students_marks[name] = scores#{"Khine":[20.0,30.0,40.0],"Zar":[20.0,30.0,40.0]}
    print(students_marks)
    query_name = input("Please enter one student: ")#Khine
    student_list = list(students_marks.keys())
    for n,s in students_marks.items():
        if n == query_name:
            print("Found")
            sumOfScores = 0
            for es in s:
                sumOfScores+=es
            print("Sum of all scores in custom student is: ",sumOfScores)
            break







