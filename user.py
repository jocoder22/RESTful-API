"""
Create a table to store user's info.

User's table.
"""

import sqlite3

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
        """Find user using username in the database"""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
