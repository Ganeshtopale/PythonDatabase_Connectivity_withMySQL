# Delete Selected Data By Mysql
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "DELETE FROM student WHERE NAME = 'Ravi'"
cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()
