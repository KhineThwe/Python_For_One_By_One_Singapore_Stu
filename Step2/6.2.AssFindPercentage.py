if __name__ == '__main__':
    n = int(input("Enter number of students"))
    students_marks = {}
    result = []
    for _ in range(n):
        name,*mark = input("Username : eg: 20 30 40").split()#Khine 20 30 40
        scores = list(map(float,mark))#[20.0,30.0,40.0]
        students_marks[name] = scores#{"Khine":[20.0,30.0,40.0],"Zar":[20.0,30.0,40.0]}
    query_name = input("Please enter one student: ")#Khine
result = students_marks[query_name]
each_scores = sum(result)/len(result)#average score
print(each_scores)





