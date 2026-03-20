import json
import datetime
import random

stdata={}
n=int(input("Enter number of students: "))
for i in range(n):
	sttime = datetime.datetime.now()
	stid=random.randint(1,1000)
	stname=input("Enter your name: ")
	stcity=input("Enter your city: ")
	stdata["time"] = sttime
	stdata["id"] = stid
	stdata["name"] = stname
	stdata["city"] = stcity
f1= open("data.json","a")
json.dump(stdata,f1)