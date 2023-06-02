def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]#second element#2
        j = i - 1#first element#5

        while j>=0 and arr[j] > key:#5>2
            arr[j+1] = arr[j]#[5,5,9,1,3]
            j -= 1

        arr[j+1] = key


if __name__ == '__main__':
    numbers = [5,2,9,1,3]
    insertion_sort(numbers)
    print(numbers)
