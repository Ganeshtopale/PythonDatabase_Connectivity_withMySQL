#UpdateByMYSQL

import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "UPDATE student SET age = 24 WHERE sid=1"
cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()
