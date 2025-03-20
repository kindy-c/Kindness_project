# Create a function for multiplication

def multiply(num1, num2):
    return num1 * num2

# Create a function to divide
def divide(num1, num2):
    return num1 / num2

# Create a function to add
def addition(num1, num2):
    return num1 + num2

# Create a function to subtract
def subtract(num1, num2):
    return num1 - num2

def calc():
    print("Welcome to my calculator")
    print("Please choose an Operation")
    while True:
        print("1. Addition", 
          "\n2. Subtraction", 
          "\n3. Division", 
          "\n4 Multiplication", "\n")
        choice = input("Please choose an operation(1-4): ")
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        if choice == "1":
            print(addition(num1, num2))
        elif choice == "2":
            print(subtract(num1, num2))
        elif choice == "3":
            print(divide(num1, num2))
        elif choice == "4":
            print(multiply(num1, num2))
        else:
            print("Invalid choice")
        response = input("Perform another operation?(yes/no): ").lower()
        if response == "no":
            break
calc()