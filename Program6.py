# importing required libraries
#Feching Or Display Particular Data From Table
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "SELECT * FROM student where age>=20"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
