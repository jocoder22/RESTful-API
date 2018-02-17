"""This is the Python app in Virtual Environment."""


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.patient import Patient, AllPatients


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

# Patients = []

# this add the resource to our api and
# define how to access the resource on our api
# to get info we use add_resource method below
# just like calling: http://127.0.0.1:5000/patient/Peter
# without the use of @app.route decorator
# no need to jsonify 'cos flask_restful does that for us


api.add_resource(Patient, '/patient/<string:name>')
api.add_resource(AllPatients, '/patients')
api.add_resource(UserRegister, '/register')

"""Run this file on the same folder with datasetup.py"""

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.debug = True
    app.run(port=5002)
