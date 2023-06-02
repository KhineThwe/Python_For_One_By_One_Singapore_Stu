#Searching algorithm
#Algorithm analysis ---> performance
def linear_search(toys,target):
    for i in range(len(toys)):
        if toys[i] == target:
            return i
    return -1

if __name__ == '__main__':
    toys = ["ball","car","doll","teddy","puzzle"]
    target_toys = input("Enter Target Toys: ")
    index = linear_search(toys,target_toys)
    print(index)
    if index != -1:
        print(f'The {target_toys} is found at index {index}')
    else:
        print(f'The {target_toys} is not found.')