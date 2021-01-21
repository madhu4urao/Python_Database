import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="password123", database="Student")
mycursor =mydb.cursor()
sqlform= "Insert into student(name, rno) values(%s,%s)"
students =[("nikhila", 192), ("amit", 183),("ankita",200), ]
mycursor.executemany(sqlform, students)
mydb.commit()