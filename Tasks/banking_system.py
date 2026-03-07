def accopen(number,name,type):
    print("Your account number is: ",number)
    print("Your account name is: ",name)
    print("Your account type is: ",type)

num1=int(input("Enter your Account number: "))
name1=input("Enter your Account name: ")
type1=input("Enter your Account type: ")

print("\nAccount Opened Successfully!\n")

def deposit():
    amt = int(input("Enter Deposit Amount: "))
    if amt >= 2000:
        print("Deposit Successful!")
    else:
        print("Minimum deposit 2000")
        
deposit()

def withdraw():
    amt = int(input("Enter Withdraw Amount: "))
    if amt <= 2000:
        print("Withdraw Successful!")
    else:
        print("Maximum withdraw 2000")
withdraw()