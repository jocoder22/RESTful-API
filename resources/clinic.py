"""
This is the file for out resources.

Resources:

"""

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.clinic import ClinicModel


class Clinic(Resource):
    """Define the resource.

    docstring for Clinic Resource.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, type=str,
                        help="This item is required!")
    # parser.add_argument('age', required=True, type=int,
    #                     help="This item is required!")
    # parser.add_argument('race', required=True, type=str,
    #                     help="Clinic id required!")
    # parser.add_argument('clinic_id', required=True, type=int,
    #                     help="This item is required!")

    @jwt_required()
    def get(self, name):
        """Define method on the resource i.e get."""
        clinic = ClinicModel.findClinic(name)
        if clinic:
            return clinic.json()
        return {'message': 'clinic {} not found in our clinic\'s database'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        """Will post data to the database."""
        if ClinicModel.findClinic(name):
            return {'message': 'clinic with name {}, already in our database'.format(name)},  400
        dataInput = Clinic.parser.parse_args()
        clinic = ClinicModel(dataInput['name'])

        try:
            clinic.insertClinic()
        except:
            return {'message': 'Error occured during insertion'}, 500
        return clinic.json(), 201

    @jwt_required()
    def delete(self, name):
        """Delete patient from the patient's database."""
        clinic = ClinicModel.findClinic(name)
        if clinic:
            clinic.deleteClinic()
            return {'message': 'clinic: {} removed from the database'
                    .format(name)}, 200
        return {'message': 'clinic with name {}, not in our database'.format(name)},  404

    @jwt_required()
    def put(self, name):
        """Update the table."""
        clinic = Clinic.parser.parse_args()
        clinic = ClinicModel.findClinic(name)

        if clinic is None:
            clinic = ClinicModel(dataget['name'])
        else:
            clinic.name = name

        clinic.insertClinic()

        return clinic.json(), 201


class ClinicList(Resource):
    """List all patients in our database.

    resource: patient database.
    """

    def get(self):
        """Return list of all patients."""
        allclinics = [clinic.json() for clinic in ClinicModel.query.all()]

        # allPatients = list(map(lambda clinic: clinic.json(), ClinicModel.query.all()))

        if len(allclinics):
            return {'Allclinics': allclinics}, 200
        return {'message': 'Clinic database is empty at this time!'}, 404
