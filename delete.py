import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="password123", database="Student")
mycursor =mydb.cursor()
sql = "DELETE FROM student WHERE name='nikhila'"
mycursor.execute(sql)
mydb.commit()