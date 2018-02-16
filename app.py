"""This is the Python app in Virtual Environment."""


from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister


app = Flask(__name__)
app.secret_key = 'bobby'
api = Api(app)         # define our api

jwt = JWT(app, authenticate, identity)

'''
   JWT creates a new endpoint '/auth',  whenever '/auth' is called with
   username  and password, the JWT extension extract the username and
   password and send them to our fucntion; authenticate and identity.
   The authenticate function compare the password and user  name with those
   in out database.
   The JWT generate and sends a token called Json Web Token, on the next
   request, the client attaches this token with the request.
   The JWT now uses the identity function to extract user id for identify
   the correct user.
'''

Patients = []

# this add the resource to our api and
# define how to access the resource on our api
# to get info we use add_resource method below
# just like calling: http://127.0.0.1:5000/patient/Peter
# without the use of @app.route decorator
# no need to jsonify 'cos flask_restful does that for us


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
        patient = next(filter(lambda x: x['name'] == name, Patients), None)
        return {'patient': patient}, 200 if patient else 404

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


api.add_resource(Patient, '/patient/<string:name>')
api.add_resource(AllPatients, '/patients')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
