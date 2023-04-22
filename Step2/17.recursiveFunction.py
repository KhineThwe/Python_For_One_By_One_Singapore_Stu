#factorial
#5! = 5*4*3*2*1 = 120
#recursive ---> function
#clean code ---> not complex
#hard to follow
#hard to debug
#iterative ---> loop
#1! = 1
#2! = 2*1
#3! = 3*2*1
def factorial(x):
    """This is a recursive function to find the factorial an integer"""
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))#5*4*3*2*1

if __name__ == '__main__':
    num = int(input("Enter num: "))
    print('The factorial of ',num,"is",factorial(num))
