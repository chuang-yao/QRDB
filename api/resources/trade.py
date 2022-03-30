import pandas as pd
from flask_restful import Resource


class Trade(Resource):
    def get(self, tid):
        """
        get trade details based on provided trade id
        :param tid:
        :return:
        """
        data = pd.read_csv('data/trades.csv', dtype={
            'TID': str, 'DateTime': str, 'Symbol': str, 'Volume': int, 'Direction': str, 'Price': float})
        data = data.set_index('TID').to_dict()
        return {'tid': tid, 'datetime': data['DateTime'][tid], 'symbol': data['Symbol'][tid],
                'volume': data['Volume'][tid], 'direction': data['Direction'][tid], 'price': data['Price'][tid]}, 200
