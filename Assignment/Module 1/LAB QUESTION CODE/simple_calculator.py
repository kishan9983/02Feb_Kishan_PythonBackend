print("1. Add")
print("2. Subtract")

choice = input("Enter choice: ")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
else:
    print("Invalid choice")