import sqlite3
"""Import sqlite. """

connection = sqlite3.connect("dataBase.db")
cursor = connection.cursor()

TableUsers = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(TableUsers)

TablePatients = "CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY, name text, sex text, age int, race text)"
cursor.execute(TablePatients)

TableClinics = "CREATE TABLE IF NOT EXISTS clinics(id INTEGER PRIMARY KEY, name text, patient INTEGER, FOREIGN KEY(patient) REFERENCES patients(id))"
cursor.execute(TableClinics)


connection.commit()
connection.close()

print("Done setting and updating database.")

"""Run the file on the folder with app.py"""
