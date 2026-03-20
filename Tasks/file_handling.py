f1 = open("file.txt", "a")

n=int(input("Enter number of Students: "))
for i in range(n):
    name = input("Enter Student Name: ")
    id = input("Enter Student ID: ")
f1.write("name:{}\n".format(name))
f1.write("id:{}\n".format(id))
