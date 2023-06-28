try:
    data = int(input("Enter a number: "))
    if data == 10:
        print("Activating exception")
        raise ZeroDivisionError
    else:
        raise TypeError
except ZeroDivisionError:
    print("From Zeror Division Error")
except TypeError:
    print("From Type Error")