n = int(input("Enter number: "))

"""
to check even number or odd number
"""
def is_even():
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

def main():
    result = is_even()
    print(type(result))
    if result == "Even number":
        print("You won")
    print(f'Result is: {result}')

if __name__ == '__main__':
    main()
