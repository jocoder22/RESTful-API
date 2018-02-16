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

    @classmethod
    def findUser(cls, username):
        """Find user."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        selectQuery = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(selectQuery, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def findUserId(cls, _id):
        """Find user using id."""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        selectQuery = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(selectQuery, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close
        return user


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

        connection = sqlite3.connect("dataBase.db")
        cursor = connection.cursor()
        insertQuery2 = "INSERT INTO users VALUES(NULL, ?, ?)"
        cursor.execute(insertQuery2, (signInData['username'],
                                      signInData['password']))
        connection.commit()
        connection.close()

        return {"message": "user now created!"}, 201
