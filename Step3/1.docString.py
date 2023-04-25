#docstring ---> documentation strings
#doc string ကို python interpreter ကသိတယ် ။ comment နဲ့မတူဘူး
#doc string သည် သူ့အပေါ်မှာ comment ကလွဲပြီးတော့ ပထမဆုံးစာကြောင်းဖြစ်ရမယ်
#dostring ---> program ကိုရှင်းရှင်းလင်းလင်းမှတ်မိပြီးတော့ စနစ်ကျ
def my_fun():
    #this function is for testing
    """
      This function is for testing
    """
    return None
    """
          This function is for testing 2
    """
print(my_fun.__doc__)