import math
def jump_search(arr,target):
    n  = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    #jump search
    while arr[min(step,n) - 1] < target:#arr[2]
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    #linear search
    while arr[prev] < target:
        prev += 1
        if prev == min(step,n):
            return -1

    if arr[prev] == target:
        return prev
    return -1

if __name__ == '__main__':
    arr = [2,5,8,12,16,23,38,56,72,91]
    target_number = int(input("Enter target number to find: "))
    index = jump_search(arr,target_number)

    if index != -1:
        print(f'Element found at index {index}')
    else:
        print(f'Element not found')