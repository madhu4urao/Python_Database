import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="password123")
mycursor =mydb.cursor()
# mycursor.execute("Create Database student")
mycursor.execute("Show Databases")
for db in mycursor:
    print(db)