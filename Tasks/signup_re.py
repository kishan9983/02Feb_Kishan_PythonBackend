import re

def signup():
    try:
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")
        password = input("Enter Password: ")
        confirm = input("Confirm Password: ")

        if (re.match("^[a-zA-Z]+$", fname) and
            re.match("^[a-zA-Z]+$", lname) and
            re.match("^[a-zA-Z0-9]+@[a-zA-Z]+\.com$", email) and
            re.match("^[0-9]{10}$", mobile) and
            re.match("^[a-zA-Z0-9]+$", password) and
            password == confirm):

            print("Signup Successful")
        else:
            print("Invalid Signup")

    except:
        print("Error Occurred")


signup()