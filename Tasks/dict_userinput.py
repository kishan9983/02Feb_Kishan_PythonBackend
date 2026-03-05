stdata={}
n=int(input("Enter the number of students: "))
for i in range(n):
    sname=input("Enter the name of student: ")
    scity=input("Enter the city of student: ")
    sid=input("Enter the id of student: ")
    stdata[sid]={
        "city":scity,
        "name":sname,
        "id":sid
 }
print(stdata)