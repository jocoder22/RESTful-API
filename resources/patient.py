"""
This is the file for out resources.

Resources:

"""

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
        if PatientModel.findPatient(name):
            return {'message': 'Patient with name {}, already in our database'.format(name)},  400
        dataInput = Patient.parser.parse_args()
        patient = PatientModel(name, dataInput['sex'], dataInput['age'],
                               dataInput['race']
                               )
        try:
            patient.insertPatient()
        except:
            return {'message': 'Error occured during insertion'}, 500
        return patient.json(), 201

    def delete(self, name):
        """Delete patient from the patient's database."""
        patient = PatientModel.findPatient(name)
        if patient:
            patient.deletePatient()
            return {'message': 'Patient: {} removed from the database'
                    .format(name)}, 200
        return {'message': 'Patient with name {}, not in our database'.format(name)},  404
        # if not PatientModel.findPatient(name):
        #     return {'message': 'Patient with name {}, not in our database'.format(name)},  404
        #
        # patient = PatientModel.findPatient(name)
        # patient.deletePatient()
        # return {'message': 'Patient: {} removed from the database'
        #         .format(name)}

    def put(self, name):
        """Update the table."""
        dataget = Patient.parser.parse_args()
        patient = PatientModel.findPatient(name)

        if patient is None:
            patient = PatientModel(name,
                                   dataget['sex'],
                                   dataget['age'],
                                   dataget['race']
                                   )
        else:
            patient.name = name
            patient.sex = dataget['sex']
            patient.age = dataget['age']
            patient.race = dataget['race']

        patient.insertPatient()

        return patient.json(), 201


class AllPatients(Resource):
    """List all patients in our database.

    resource: patient database.
    """

    def get(self):
        """Return list of all patients."""
        allPatients = [patient.json() for patient in PatientModel.query.all()]

        # allPatients = list(map(lambda patient: patient.json(), PatientModel.query.all()))

        if len(allPatients):
            return {'AllPatients': allPatients}, 200
        return {'message': 'Patient database is empty at this time!'}, 404
