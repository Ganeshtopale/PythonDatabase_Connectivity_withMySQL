# importing required libraries
#Creating a table
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root",
database = "admin"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE student(
				sid INT NOT NULL Primary Key,
				name VARCHAR(20) NOT NULL,
				age INT
				)"""

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()
