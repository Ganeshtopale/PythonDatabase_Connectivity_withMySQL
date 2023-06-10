# importing required libraries
#inserting single data in table
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

sql = "INSERT INTO student (sid, name, age)\
VALUES (%s, %s, %s)"
val = ("1", "Ravi", "20")

cursorObject.execute(sql, val)
dataBase.commit()

# disconnecting from ser                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ver
dataBase.close()
