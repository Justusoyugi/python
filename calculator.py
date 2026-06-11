import os
os.system('cls' if os.name == 'nt' else 'clear')


def add(x, y):
    return (x + y)


def subtract(x, y):
    return (x - y)


def divide(x, y):
    return (x / y)


def multiply(x, y):
    return (x * y)


print("-----Calculator-----")

print("\n 1. Add ->"
      "\n 2. Subtract ->"
      "\n 3. Divide ->"
      "\n 4. Multiply ->"
      "\n 5. Exit ->")


while True:
    a = input("\n Which arithmeric would you like to perform? ")

    if a == "1":
        print("\nAddition:")
        x = int(input("What's your first value? "))
        y = int(input("What's your second value? "))
        print("\nThe answer is ", add(x, y))
        continue
    elif a == "2":
        print("\nSubtraction:")
        x = int(input("What's your first value? "))
        y = int(input("What's your second value? "))
        print("\nThe answer is ", subtract(x, y))
        continue
    elif a == "3":
        print("\nDivision:")
        x = int(input("What's your first value? "))
        y = int(input("What's your second value? "))
        print("The answer is ", divide(x, y))
        continue
    elif a == "4":
        print("\nMultiplication:")
        x = int(input("What's your first value? "))
        y = int(input("What's your second value? "))
        print("\nThe answer is ", add(x, y))
        continue
    elif a == "5":
        print("Goodbye.")
        break
    else:
        print("\nPlease choose between 1-5.")
