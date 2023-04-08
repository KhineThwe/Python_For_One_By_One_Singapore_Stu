#condition
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
new_list = [num for num in numbers if num % 2 == 0]
odd_list = [num for num in numbers if num % 2 != 0]
print(new_list)
print(odd_list)

#nested condition
new_list1 = [num for num in numbers if num %2 == 0 if num %3 ==0]#2 4 6 8 10 12
print(new_list1)

#if else in list comprehension
new_list2 = [num*2 if num%2 ==0 else num for num in numbers]
#odd number will return same but even will be double
print(new_list2)