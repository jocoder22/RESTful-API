"""This is the Python app in Virtual Environment."""


from flask import flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Patient(Resource):
    """docstring for Patient.Resource."""
    def get(self, name):
        return {'patient': name}


# to get info we use the below
# just like calling: http://127.0.0.1:5000/student/Rolf
# not use of @app.route again
api.add_resource(Patient, '/patient/<string:name>')




if __name__ = '__main__':
    app.debug = True
    app.run(port=5000)
