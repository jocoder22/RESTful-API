"""
This is the file for out patient model.

Models:

"""

import sqlite3
from db import db

class PatientModel(db.Model):
    """Docstring for PatientModel.

    Patient Model:

    """

    __tablename = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    sex = db.Column(db.String(80))
    age = db.Column(db.Integer(80))
    race = db.Column(db.String(80))


    def __init__(self, name, sex , age, race):
        """Initialize the class."""
        self.name = name
        self.sex = sex
        self.age = age
        self.race = race

    def json(self):
        """Return json representation of our object"""
        return {'name': self.name, 'sex': self.sex, 'age': self.age, 'race': self.race}

    @classmethod
    def findPatient(cls, name):
        """Define method on the resource i.e get."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        getQuery = "SELECT * FROM patients WHERE name=?"
        result = cursor.execute(getQuery, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)

    def insertPatient(self):
        """Insert into database."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()
        insertQuery = "INSERT INTO patients VALUES(?, ?, ?, ?)"
        cursor.execute(insertQuery, (self.name, self.sex, self.age, self.race))

        connection.commit()
        connection.close()

    def updatePatient(self):
        """Update database."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()
        updateQuery = "UPDATE patients SET name=?, sex=?, age=?, race=? WHERE name=?"
        cursor.execute(updateQuery, (self.name, self.sex, self.age, self.race, self.name))

        connection.commit()
        connection.close()
