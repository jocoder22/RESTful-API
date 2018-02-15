"""This is the Python app in Virtual Environment."""


from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)         # define our api

Patients = []


class Patient(Resource):   # define the resource
    """docstring for Patient.Resource."""
    def get(self, name):        # define method on the resource i.e get
        for patient in Patients:
            if patient['name'] == name:
                return patient, 200
        return {'patient': None}, 404  # define the result when api is called

    def post(self, name):
        patient = {
                    'name': 'Jemmy',
                    'sex': 'male',
                    'age': 54,
                    'race': 'black'
                    }
        Patients.append(patient)
        return patient, 201  # no need to jsonify 'cos flask_restful does that for us


# this add the resource to our api and
# define how to access the resource on our api
# to get info we use add_resource method below
# just like calling: http://127.0.0.1:5000/patient/Peter
# without the use of @app.route decorator
api.add_resource(Patient, '/patient/<string:name>')




if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
