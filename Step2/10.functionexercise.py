def return_day(num):
    match num:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
if __name__ == '__main__':
    day = int(input("Enter number to return: "))
    return_day(day)