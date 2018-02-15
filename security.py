"""" This will create the user table database.

Create file for storing user info.
"""

from werkzeug.security import safe_str_cmp
from user import User

# users = [
#     User(1, 'james', 'funny')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # user1 = username_mapping.get(username, None)
    user1 = User.findUser(username)
    if user1 and safe_str_cmp(user1.password, password):
        return user1


def identity(payload):
    user_id = payload['identity']
    # return userid_mapping.get(user_id, None)
    return User.findUserId(user_id)
