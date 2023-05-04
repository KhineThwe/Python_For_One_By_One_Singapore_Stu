#1.set the first element as minimum
#2.Compare the minimum element with second element
   # If the second element is smaller than minimum,assign the second element as minimum
   #After each iteration,minimum is placed in the front of the unsort list.

def selectionSort(array,size):
    for i in range(size):#array = [20,12,10,15,2]
        minimum_index = i
        for j in range(i+1,size):
            if array[j] < array[minimum_index]:#15<12
                minimum_index = j

        #swap
        (array[i],array[minimum_index]) = (array[minimum_index],array[i])


if __name__ == "__main__":
    data = [20,12,10,15,2]
    size = len(data)
    selectionSort(data,size)
    print("Sorted array in Ascending order: ",data)