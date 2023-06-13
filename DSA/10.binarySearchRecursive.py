def binary_search(arr,target,low,high):
    if low <= high:
        mid = (low+high)//2

        if  target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binary_search(arr,target,mid+1,high)
        else:
            return binary_search(arr,target,low,mid-1)
    return -1
if __name__ == '__main__':
    arr = [2,4,7,11,15,18,23,27]
    target = int(input("Enter your target: "))
    result = binary_search(arr,target,0,len(arr)-1)
    if result != -1:
        print(f'Element found at index {result}')
    else:
        print(f'Element not found')

