import pandas as pd
from flask_restful import Resource


class User(Resource):
    def get(self, uid):
        """
        get user info based on provided user id
        :param uid:
        :return:
        """
        data = pd.read_csv('data/users.csv', dtype={'Name': str, 'UID': str, 'Email': str, 'Password': str})
        data = data.set_index('UID').to_dict()
        return {'uid': uid, 'name': data['Name'][uid], 'email': data['Email'][uid], 'password': '########'}, 200
