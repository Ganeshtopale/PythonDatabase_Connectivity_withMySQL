#OrderByClauseByMYSQL
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
