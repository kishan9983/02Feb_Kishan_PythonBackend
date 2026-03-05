list1 = ['apple', 'banana', 'mango']
search = "banana"

for item in list1:
    if item == search:
        print("Found")
        break
else:
    print("Not Found")