number = int(input("Enter number: "))
calc = lambda number:"Even number" if number%2 ==0 else "Odd number"
print(calc(number))