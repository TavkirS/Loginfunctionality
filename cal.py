print("Simple Calculator - Version 2")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("3. BOD")
print("4. Percentage")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid choice")
