from mysql import connector

dataBase = connector.connect(
    host = 'localhost',
    user = 'root',
    password = "*222bda03jason*",
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('create database if not exists knowledgekeepdb')

print('All done!!')