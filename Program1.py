# importing required libraries
#Connetion Checking In Python
import mysql.connector

dataBase = mysql.connector.connect(
host ="127.0.0.1",
user ="root",
passwd ="root"
)

print(dataBase)

# Disconnecting from the server
dataBase.close()
