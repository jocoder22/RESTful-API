"""
Create a table to store user's info.

User's table.
"""

import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    """docstring for user.

    user's table.
    """

    def __init__(self, _id, username, password):
        """Initialize the class."""
        self.id = _id
        self.username = username
        self.password = password


class UserRegister(Resource):
    """docstring for UserRegister."""

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, type=str,
                        help="This item is required!")
    parser.add_argument('password', required=True, type=str,
                        help="This item is required!")

    def post(self):
        """Post to register users."""
        connection = sqlite3.connect("dataBase.db")
        cursor = connection.cursor()
        signInData = (UserRegister.parser.parse_args())
        insertQuery2 = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(insertQuery2, *signInData)
        connection.commit()
        connection.close()

        return {"message": "user now created!"}, 201
