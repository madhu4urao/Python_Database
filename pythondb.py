import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="password123", database="Student")
mycursor =mydb.cursor()
# mycursor.execute("Create table Student(name varchar(200), rno int(20))")
mycursor.execute("Show tables")
for tb in mycursor:
    print(tb)