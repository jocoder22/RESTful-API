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


    def findUser(self, username):
        """Find user using username in the database"""
        connection = sqlite3.connect('dataBase.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user
