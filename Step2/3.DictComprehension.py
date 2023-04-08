#Dictionary Comprehension
my_dictionary = {"firstName":"Harry","lastName":"Potter"}
my_new_item = {"first":1,"second":2,"third":3}
new_dictionary ={k:v*2 for k,v in my_new_item.items()}
print(new_dictionary)

#List to dictionary comprehension
my_new_list = [1,2,3,4,5]
new_dictionary1 = {num:num*2 for num in my_new_list}
print(type(new_dictionary1))#dict
print(new_dictionary1)