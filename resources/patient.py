"""
This is the file for out resources.

Resources:

"""

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.patient import PatientModel


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
        patient = PatientModel.findPatient(name)
        if patient:
            return patient.json(), 200
        return {'message': 'Patient {} not found in our patient\'s database'.format(name)}, 404

    def post(self, name):
        """Will post data to the database."""
        # if next(filter(lambda x: x['name'] == name, Patients), None):
        if PatientModel.findPatient(name):
            return {'message': 'Patient with name {}, already in our database'.format(name)},  400
        dataInput = Patient.parser.parse_args()
        patient = PatientModel(name,
                               dataInput['sex'],
                               dataInput['age'],
                               dataInput['race']
                               )
        try:
            patient.insertPatient()
        except:
            return {'message': 'Error occured during insertion'}, 500
        return patient, 201

    def delete(self, name):
        """Delete patient from the patient's database."""
        if not PatientModel.findPatient(name):
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
        patient = PatientModel.findPatient(name)

        Updatedpatient = PatientModel(name,
                                      dataget['sex'],
                                      dataget['age'],
                                      dataget['race']
                                      )
        if patient is None:
            try:
                Updatedpatient.insertPatient()
            except:
                return {'message': 'Error with insertion'}, 500

        else:
            try:
                Updatedpatient.updatePatient()
            except:
                return {'message': 'Error with updating'}, 500
        return Updatedpatient.json(), 201


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

        allPatients = []

        if len(result):
            for row in result:
                allPatients.append({'name': row[0], 'sex': row[1], 'age': row[2], 'race': row[3]})

            return {'AllPatients': allPatients}, 200
        connection.close()
        return {'message': 'Patient database is empty at this time!'}, 201
