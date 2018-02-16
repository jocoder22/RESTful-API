"""
This is the file for out resources.

Resources:

"""

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Patient(Resource):
    """Define the resource.

    docstring for Patient Resource.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('sex', required=True, type=str,
                        help="This item is required!")
    parser.add_argument('age', required=True, type=int,
                        help="This item is required!")
    parser.add_argument('race', required=True, type=str,
                        help="This item is required!")

    @jwt_required()
    def get(self, name):
        """Define method on the resource i.e get."""
        patient = Patient.findPatient(name)
        if patient:
            return patient, 200
        return {'message': 'Patient {} not found in our patient\'s database'.format(name)}, 404

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
            return {'Patient': {'name': row[0], 'age': row[1], 'sex': row[2], 'race': row[3]}}

    def post(self, name):
        """Will post data to the database."""
        # if next(filter(lambda x: x['name'] == name, Patients), None):
        if Patient.findPatient(name):
            return {'message': 'Patient with name {}, already in our database'.format(name)},  400
        dataInput = Patient.parser.parse_args()
        patient = {
                    'name': name,
                    'sex': dataInput['sex'],
                    'age': dataInput['age'],
                    'race': dataInput['race']
                    }
        try:
            Patient.insertPatient(patient)
        except:
            return {'message': 'Error occured during insertion'}, 500
        return patient, 201

    @classmethod
    def insertPatient(cls, patient):
        """Insert into database."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()
        insertQuery = "INSERT INTO patients VALUES(?, ?, ?, ?)"
        cursor.execute(insertQuery, (patient['name'], patient['sex'], patient['age'], patient['race']))

        connection.commit()
        connection.close()

    def delete(self, name):
        """Delete patient from the patient's database."""
        if not Patient.findPatient(name):
            return {'message': 'Patient with name {}, not in our database'.format(name)},  404

        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()
        deleteQuery = "DELETE FROM patients WHERE name=?"
        cursor.execute(deleteQuery, (name,))

        connection.commit()
        connection.close()
        return {'message': 'Patient: {} removed from the database'
                .format(name)}

    def put(self, name):
        """Update the table."""
        dataget = Patient.parser.parse_args()
        patient = Patient.findPatient(name)

        Updatedpatient = {
                    'name': name,
                    'sex': dataget['sex'],
                    'age': dataget['age'],
                    'race': dataget['race']
                    }
        if patient is None:
            try:
                Patient.insertPatient(Updatedpatient)
            except:
                return {'message': 'Error with insertion'}, 500

        else:
            try:
                Patient.updatePatient(Updatedpatient)
            except:
                return {'message': 'Error with updating'}, 500
        return Updatedpatient, 201

    @classmethod
    def updatePatient(cls, patient):
        """Update database."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()
        updateQuery = "UPDATE patients SET name=?, sex=?, age=?, race=? WHERE name=?"
        cursor.execute(updateQuery, (patient['name'], patient['sex'], patient['age'], patient['race'], patient['name']))

        connection.commit()
        connection.close()


class AllPatients(Resource):
    """List all patients in our database.

    resource: patient database.
    """

    def get(self):
        """Return list of all patients."""
        # return {'Patients': Patients}
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        getQuery = "SELECT * FROM patients"
        result = cursor.execute(getQuery)
        row = result.fetchall()
        connection.close()

        if row:
            # return {'Patients': row}
            # allUsers=[i.serialize for i in users],
            return row
        return {'message': 'Patient database is empty at this time!'}
