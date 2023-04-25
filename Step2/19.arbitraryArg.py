def avg(*args):
    length = len(args)#0
    total = sum(args)#0
    if length == 0:
        return 0
    else:
        return total/length#15/5 ===> 3.0

result = avg(1,2,3,4,5)
print("Result: ",result)