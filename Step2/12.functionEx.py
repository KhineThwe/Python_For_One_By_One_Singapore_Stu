def return_day(num):#num=7
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num>0 and num<8:
        return days[num-1]#num= 7 days[6]
    else:
        return "Invalid number"

if __name__ == '__main__':
    day = int(input("Enter number to return: "))
    print(return_day(day))