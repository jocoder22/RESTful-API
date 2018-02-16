import sqlite3
"""Import sqlite. """

connection = sqlite3.connect("dataBase.db")
cursor = connection.cursor()

TableUsers = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(TableUsers)

TablePatients = "CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY, name text, age int, sex text, race text)"
cursor.execute(TablePatients)

# insertQuery3 = "INSERT INTO patients VALUES('Jemmy', 56, 'male', 'white')"
# cursor.execute(insertQuery3)

# user = (1, 'james', 'funny')
# insertQuery = "INSERT INTO users VALUES(?, ?, ?)"
# cursor.execute(insertQuery, user)
#
# users = [
#     (2, 'john', 'seaman'),
#     (3, 'jane', 'goodlady'),
#     (4, 'mary', 'motherlove')
# ]
# cursor.executemany(insertQuery, users)

connection.commit()
connection.close()

print("Done setting and updating database.")

"""Run the file on the folder with app.py"""
