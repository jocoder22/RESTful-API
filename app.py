"""This is the Python app in Virtual Environment."""


from flask import flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Patient(Resource):
    """docstring for Patient.Resource."""
    def get(self, name):
        return {'patient': name}


# to get info we use add_resource method below
# just like calling: http://127.0.0.1:5000/patient/Peter
# without the use of @app.route decorator
api.add_resource(Patient, '/patient/<string:name>')




if __name__ = '__main__':
    app.debug = True
    app.run(port=5000)
