"""" This will create the user table database.

Create file for storing user info.
"""

from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user1 = UserModel.findUser(username)
    if user1 and safe_str_cmp(user1.password, password):
        return user1


def identity(payload):
    user_id = payload['identity']
    return UserModel.findUserId(user_id)
