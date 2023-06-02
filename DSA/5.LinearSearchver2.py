#Searching algorithm
#Algorithm analysis ---> performance
def linear_search(array,n,x):
    for i in range(0,n):
        if array[i] == x:
            return i
    return -1


if __name__ == '__main__':
    nums = [2,5,10,11,15,16,17,19,25,30,40]
    key = int(input("Enter key to find: "))
    n = len(nums)
    result = linear_search(nums,n,key)
    if result != -1:
        print(f'The {key} is found at index {result}')
    else:
        print(f'The {key} is not found.')

