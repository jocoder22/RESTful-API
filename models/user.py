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