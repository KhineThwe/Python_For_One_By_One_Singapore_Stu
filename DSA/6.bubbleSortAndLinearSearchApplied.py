def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

def linear_search(numbers,target_number):
    print(numbers)
    for number in numbers:
        if number == target_number:
            return True
    return False

# def linear_search(array,n,x):
#     for i in range(0,n):
#         if array[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    numbers_list = [5,2,8,1,3,9]
    target_number = int(input("Enter your number to search: "))
    bubble_sort(numbers_list)
    print("After Sorting list: ",numbers_list)
    n = len(numbers_list)

    # index = linear_search(numbers_list,n,target_number)
    is_found = linear_search(numbers_list,target_number)

    if is_found:
        print(f'The number {target_number} is found in the list!')
    else:
        print(f'The number {target_number} is not found in the list!')