"""Import db."""
import sqlite3
from db import db


class UserModel(db.Model):
    """docstring for user.

    user's table.

    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        """Initialize the class."""
        self.username = username
        self.password = password

    def saveData(self):
        """Save data to database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findUser(cls, username):
        """Find user."""
        return cls.query.filter_by(username=username).first()

    @classmethod
    def findUserId(cls, _id):
        """Find user using id."""
        return cls.query.filter_by(id=_id).first()
