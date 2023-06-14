#Bitwise XOR ^ တူရင် 0 မတူရင် 1
# x y | output
# 0 0 | 0
# 0 1 | 1
# 1 0 | 1
#1  1 | 0
a = 5
b = 3
c = a ^ b
print("XOR result: ",c)

#1 0 1
#0 1 1
#===========
#1  1  0
#=6

#Left shift <<
#value increase
#ညာဘက်ကနေ 0 ဝင်မယ်။
# int data.txt 32 bits
x = 20
y = x << 4
print("After left shift: ",y)
#8bits = 1byte
#0000 0000 0000 0000 0000 0000 0001 0100
#After left shift
#0000 0000 0000 0000 0000 0001 0100 0000


#Right shift >>
#value decrease
#ဘယ်ဘက်ကနေ 0 ဝင်ရမည်။
x = 20
y = x >> 4
print("After Right shift: ",y)

#0000 0000 0000 0000 0000 0000 0001 0100
#After Right shift
#0000 0000 0000 0000 0000 0000 0000 0001
