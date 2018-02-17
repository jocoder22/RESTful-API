"""
Create a table to store user's info.

User's table.
"""

from flask_restful import Resource, reqparse
from models.user import UserModel


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
        if UserModel.findUser(signInData['username']):
            return {'message': 'User {} already exist, choose another username'.format(signInData['username'])}, 400

        # user = UserModel(signInData['username'],
        #                               signInData['password']))
        user = UserModel(**signInData)
        user.saveData()

        return {"message": "user now created!"}, 201
