#declare
#def ---> keyword
#function_name --> get_choice
#() --->(parameters)
#function မှာ function 2 မျိုး ရှိတယ်။
#return ပြန်တဲ့ function return မပြန်တဲ့ function
#function တွေက သူတို့သည် လှမ်းခေါ်မှသာ အလုပ်လုပ်သည်။
#function လှမ်းခေါ်တဲ့အခါ function ရဲ့ name နဲ့လှမ်းခေါ်မှသာ အလုပ်လုပ်မည်။
#function စစရေး တဲံအခါမှာ parameter ပါရင် parameter ကို ထည့်ပြီးတော့လှမ်းခေါ်ရမည်။

def function_name():#return မပြန်သော function
    #function body
    print("Hi Function")

#လှမ်းခေါ်တဲ့နေရာ
function_name()


def function_name1():#return ပြန်သော function
    #function body
    return "Hi Function1"

#လှမ်းခေါ်တဲ့နေရာ
a = function_name1()
print(a)

def function_name2(name,age):
    print("Hi Function2",name,":",age)

#လှမ်းခေါ်တဲ့နေရာ
function_name2("Google",20)

