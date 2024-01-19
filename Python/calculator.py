def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error, can not divided by 0"
    else:
        return num1 / num2

def calculator():
    print("Select operation")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice number:")

    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice == "1":
        print(add(num1, num2))
    elif choice == "2":
        print(sub(num1, num2))
    elif choice == "3":
        print(multiply(num1, num2))
    elif choice == "4":
        print(divide(num1, num2))
    else:
        print("Invalid number")

calculator()


import random

def roll_dice():
    return random.randrange(1, 7)

print(roll_dice())
print(roll_dice())
print(roll_dice())
print(roll_dice())
