# importing required libraries

#Display  data from table
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "select sid,name,age from student"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
