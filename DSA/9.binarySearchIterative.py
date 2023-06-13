def binary_search(arr,target):
    low = 0
    high = len(arr) - 1

    #iterative method
    while low <=high:
        # mid = (low+high)//2
        mid =low+ (high - low) // 2

        if target == arr[mid]:
            return mid#return index
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    #array must be sorted
    arr = [2,4,7,11,15,18,23,27]
    target = int(input("Enter your target element: "))

    result = binary_search(arr,target)

    if result != -1:
        print(f'Element found at index {result}')
    else:
        print(f'Element not found')


