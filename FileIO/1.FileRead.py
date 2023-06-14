"""
read       ----> return string
readline     -----> return string
readlines    ---->  return list

open("fileName","fileMode")
fileMode ---> r ----> read
         ---> w ----> write
         ---> a ---> append
"""
file = open('data.txt','r')
if file:
    print("Success of opening file")
    # data = file.readlines()
    # print("Reading data with readlines")
    # print(data)
    # print(type(data))

    # data1 = file.readline()
    # print("Reading data with readline")
    # print(data1)
    # print(type(data1))

    data1 = file.read()
    print("Reading data with read")
    print(data1)
    print(type(data1))
else:
    print("Error")
file.close()

