
def remainder_division():
    number1: int = int(input("Enter the first number: "))
    number2: int = int(input("Enter the second number: "))
    
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        remainder: int = number1 % number2
        print(f"The remainder of {number1} divided by {number2} is {remainder}")

remainder_division()
