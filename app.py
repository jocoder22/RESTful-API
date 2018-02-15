"""This is the Python app in Virtual Environment."""


from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'josee'
api = Api(app)         # define our api

jwt = JWT(app, authenticate, identity)

'''
   JWT creates a new endpoint '/auth',  whenever '/auth' is called with
   username  and password, the JWT extension extract the username and
   password and send them to our fucntion; authenticate and identity.
   
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

    def get(self, name):
        """Define method on the resource i.e get."""
        patient = next(filter(lambda x: x['name'] == name, Patients), None)
        return {'patient': patient}, 200 if patient else 404

    def post(self, name):
        """Will post data to the database."""
        if next(filter(lambda x: x['name'] == name, Patients), None):
            return {'message': 'Patient with name {}, already in our database'
                    .format(name)},  400
        dataInput = request.get_json()
        patient = {
                    'name': name,
                    'sex': dataInput['sex'],
                    'age': dataInput['age'],
                    'race': dataInput['race']
                    }
        Patients.append(patient)
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


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
