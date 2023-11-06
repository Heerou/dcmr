import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234'
)


#cursor obj
cursorObject = database.cursor()
#execute cursor obj to create db
cursorObject.execute("CREATE DATABASE elderco")

print("Done!")