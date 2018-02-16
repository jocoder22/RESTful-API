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
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        getQuery = "SELECT * FROM patients WHERE name=?"
        result = cursor.execute(getQuery, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'Patient': {'name': row[0], 'age': row[1], 'sex': row[2], 'race': row[3]}}, 200
        return {'message': 'Patient {} not found in our patient\'s database'.format(name)}, 404

    def post(self, name):
        """Will post data to the database."""
        if next(filter(lambda x: x['name'] == name, Patients), None):
            return {'message': 'Patient with name {}, already in our database'
                    .format(name)},  400
        dataInput = Patient.parser.parse_args()
        patient = {
                    'name': name,
                    'sex': dataInput['sex'],
                    'age': dataInput['age'],
                    'race': dataInput['race']
                    }
        Patients.append(patient)
        return patient, 201

    def delete(self, name):
        """Delete patient from the patient's database."""
        global Patients
        Patients = list(filter(lambda x: x['name'] != name, Patients))
        return {'message': 'Patient: {} removed from the database'
                .format(name)}

    def put(self, name):
        """Update the table."""
        dataget = Patient.parser.parse_args()
        patient = next(filter(lambda x: x['name'] == name, Patients), None)
        if patient is None:
            patient = {
                        'name': name,
                        'sex': dataget['sex'],
                        'age': dataget['age'],
                        'race': dataget['race']
                        }
            Patients.append(patient)
        else:
            patient.update(dataget)
        return patient, 201


class AllPatients(Resource):
    """List all patients in our database.

    resource: patient database.
    """

    def get(self):
        """Return list of all patients."""
        return {'Patients': Patients}
