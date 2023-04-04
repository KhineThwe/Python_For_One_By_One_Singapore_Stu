print("""
  My name 
  is 
  Khine
""".upper())
print("""
  My name 
  is 
  Khine
""".lower())
#strip ---> remove whitespace from beginning and end
a = " HelloW orld "
print(a.strip())
print(a.replace("He","he"))
print(a.split(" "))
#concatenate
a = "H"
b = "U"
result = a + b

#format
age = 24
txt = "My name is John,and I am {}"
print(txt.format(age))

#isapha()---> to check alphabet ?
example = "Python@#!"
print(example.isalpha())

#isalnum() ---> alphabet letter (a-z) and numbers (0-9).
example = "Python7012#"
print(example.isalnum())

#isdecimal()---> digits ?
#startswith ---> string starts with specific substring
#endswith ----> string ends with specific substring
example = "Python7012#"
print(example.startswith("P"))
print(example.endswith("#"))
print(example.find("#"))#returns index number