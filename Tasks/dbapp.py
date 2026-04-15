import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='pov')
    print("Database connected successfully")
except Exception as e:
    print("Error connecting to database:", e)

cr=db.cursor()

create_table="CREATE TABLE studinfo(id integer primary key auto_increment,name varchar(20), city varchar(20))"

try:
    cr.execute(create_table)
    print("Table Created")
except Exception as e:
    print(e)

"""insert_data="INSERT INTO studinfo(name,city) VALUES('Kishan','Rajkot'),('Krish','surat'),('kartik','bhavnagar'),('jash','amreli'),('Tirth','Navasari')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Data Inserted")
except Exception as e:
    print(e)"""

update_data="UPDATE studinfo SET city='Ahmedabad' WHERE name='Kishan'"
try:
    cr.execute(update_data)
    db.commit()
    print("Data Updated")
except Exception as e:
    print(e)

delete_data="DELETE FROM studinfo WHERE name='Tirth'"
try:
    cr.execute(delete_data)
    db.commit()
    print("Data Deleted")
except Exception as e:
    print(e)