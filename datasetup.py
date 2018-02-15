import sqlite3

connection = sqlite3.connect("dataBase.db")

cursor = connection.cursor()

createTable = "CREATE TABLE users(id int, username text, password text)"
cursor.execute(createTable)

user = (1, 'james', 'funny')
insertQuery = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insertQuery, user)

users = [
    (2, 'john', 'seaman'),
    (3, 'jane', 'goodlady'),
    (4, 'mary', 'motherlove')
]
cursor.executemany(insertQuery, users)

connection.commit()
connection.close()

print 'Done setting and updating database'
