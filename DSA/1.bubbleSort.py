def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                #swap
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

if __name__ == '__main__':
    data = [-2,45,0,11,-9]
    bubbleSort(data)
    print('Sorted array with bubble sort',data)

#5-0-1 = 4 ---> j=0,1,2,3
#nested loop ရဲ့သဘောတရားအရ အတွင်း loop ပီးတာနဲ့ အပြင်loop သွား

#i = 1
# j = 5-1-1 = 3,j===> 0,1,2

#i = 2
#j = 5-2-1 = 2 , j===> 0,1

#i = 3
#j = 5-3-1 = 1,j==> 0

#i = 4
#j = 5-4-1 = 0