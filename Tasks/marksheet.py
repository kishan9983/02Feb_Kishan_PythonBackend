subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))
subject4 = int(input("Enter marks of subject 4: "))
total = subject1 + subject2 + subject3 + subject4
print("Total Marks:", total)
percentage = total / 4
print("Percentage:", percentage)

if percentage >= 70:
    print("Grade: A+")
elif percentage >= 60:
    print("Grade: A")
elif percentage >= 50:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Fail")