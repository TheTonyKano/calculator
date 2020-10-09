num1 = ""
num2 = ""
total = ""


def add(num1, num2):
    global total
    total = num1 + num2
    return total


def subtract(num1, num2):
    global total
    total = num1 - num2
    return total


def multiply(num1, num2):
    global total
    total = num1 * num2
    return total


def divide(num1, num2):
    global total
    total = num1 / num2
    return total


def user_input():
    global num1
    global num2
    num1 = float(input("Please enter a number :"))
    num2 = float(input("Please enter another number :"))
    return num1, num2

while True:
    print("If you want to add two numbers, please type 'add'")
    print("If you want to subtract two numbers, please type 'subtract'")
    print("If you want to divide two numbers, please type 'divide'")
    print("If you want to multiply two numbers, please type 'multiply'")
    print("If you want to end the program, please type 'quit'")
    choice = input("Please type your choice: ")

    if choice == 'add':
        user_input()
        add(num1, num2)
        print(num1, "+", num2, "=", total)

    elif choice == 'subtract':
        user_input()
        subtract(num1, num2)
        print(num1, "-", num2, "=", total)

    elif choice == 'multiply':
        user_input()
        multiply(num1, num2)
        print(num1, "*", num2, "=", total)

    elif choice == 'divide':
        user_input()
        divide(num1, num2)
        print(num1, "/", num2, "=", total)

    elif choice == "quit":
        break

    else:
        print("Unknown input")
