class student:
    def printdata(self,id,name):
        print("id:",id)
        print("name:",name)

s1=student()

id=int(input("enter id:"))
name=input("enter name:")
s1.printdata(id,name)