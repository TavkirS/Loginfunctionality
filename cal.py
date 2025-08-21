print("Simple Calculator - Version 1")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice (1/2): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

else:
    print("Invalid choice")
