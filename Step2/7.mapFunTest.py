def addition(n):#1#2#3#4#5
    return n +n#1+1=2#2+2=4#3+3=6#4+4=8#5+5=10
if __name__ == '__main__':
    numbers = (1, 2, 3, 4, 5)
    result = map(addition, numbers)
    # map fun returns map object
    print(list(result))

#2 4 6 8 10 ---> output