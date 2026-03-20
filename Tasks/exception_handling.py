try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:",a+b)
except Exception as e:  
    print(e)
else:
    print("No exception occurred")
finally:
    print("This block will always execute")
    