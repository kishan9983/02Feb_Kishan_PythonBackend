

n = int(input("Enter number of students: "))
for i in range(n):
    sid = input("Enter student id: ")
    sname = input("Enter student name: ")
    scity = input("Enter student city: ")

    ids[i] = sid
    names[i] = sname
    cities[i] = scity
print("id =",(ids.values()))
print("name =",(names.values()))
print("city =",(cities.values()))