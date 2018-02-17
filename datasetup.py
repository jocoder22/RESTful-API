import sqlite3
"""Import sqlite. """

connection = sqlite3.connect("dataBase3.db")
cursor = connection.cursor()

TableUsers = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(TableUsers)

TablePatients = "CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY, name text, sex text, age int, race text)"
cursor.execute(TablePatients)

connection.commit()
connection.close()

print("Done setting and updating database.")

"""Run the file on the folder with app.py"""
