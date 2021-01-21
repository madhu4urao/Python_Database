import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="password123", database="Student")
mycursor =mydb.cursor()
sql = "Update student SET rno =139 WHERE name='nikhila'"
mycursor.execute(sql)
mydb.commit()