#Bitwise operator 6 ခုရှိတယ်။
#1.Bitwise(&) And
#2.Bitwise(|) or
#3.Bitwise (~) Not or One's Complement
#4.Bitwise (^) Xor
#5.Bitwise (>>) right shift
#6.Bitwise (<<) left shift
#==============================================

#Bitwise (&) And ------> and
#logical Op နဲ့အနည်းငယ်ဆင်တယ်။
#x y | xy(output)
#0 False 1 True
#0 0 | 0
#0 1 | 0
#1 0 | 0
#1 1 | 1
#Bitwise operator သည် bit by bit operation ဖြစ်သည်။ Bit တစ်ခုချင်းစီလုပ်ပေးတာ
#Decimal ကနေ Binary value ချိန်းပြီးတော့မှ operation ပြုလုပ်ပေးရမည်။
#အဲ့လိုပြောင်းဖို့ ဆိုရင် 2 နှင့်ထိုပြောင်းမည့် value ကိုစားရန်လိုအပ်ပါသည်။

#8 bit = 1 byte
a = 60
b = 13
c = 0
c = a & b
print("bitwise and operation",c)
#hello   olleh