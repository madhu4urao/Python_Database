import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="password123", database="Student")
mycursor =mydb.cursor()
# mycursor.execute("Select name from student")
mycursor.execute("Select * from student")
# myresult =mycursor.fetchone()
myresult =mycursor.fetchall()
for row in myresult:
    print(row)