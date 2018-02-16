"""
Create a table to store user's info.

User's table.
"""

import sqlite3
from flask_restful import Resource, reqparse


class UserRegister(Resource):
    """docstring for UserRegister."""

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, type=str,
                        help="This item is required username")
    parser.add_argument('password', required=True, type=str,
                        help="This item is required!")

    def post(self):
        """Post to register users."""
        signInData = UserRegister.parser.parse_args()
        if User.findUser(signInData['username']):
            return {'message': 'User {} already exist, choose another username'.format(signInData['username'])}, 400

        connection = sqlite3.connect("dataBase.db")
        cursor = connection.cursor()
        insertQuery2 = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(insertQuery2, (signInData['username'],
                                      signInData['password']))
        connection.commit()
        connection.close()

        return {"message": "user now created!"}, 201
