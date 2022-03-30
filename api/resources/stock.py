import pandas as pd
from flask_restful import Resource, reqparse, abort
from api.common.util import symbol_exists


class Stock(Resource):
    def get(self, symbol):
        """
        return price data for given date, symbol, and field
        :param symbol:
        :return:
        """
        if symbol_exists(symbol):
            data = pd.read_csv('data/' + symbol + '.csv')
            data = data.set_index('Date').to_dict()

            parser = reqparse.RequestParser()
            parser.add_argument('field', required=True)
            parser.add_argument('date.beg', required=True)
            parser.add_argument('date.end', required=False)
            args = parser.parse_args()

            results = {}
            current_date = pd.to_datetime(args['date.beg'])
            end_date = current_date
            if args['date.end'] is not None:
                end_date = pd.to_datetime(args['date.end'])
            while current_date <= end_date:
                if current_date.strftime('%Y-%m-%d') in data[args['field']]:
                    results[current_date.strftime('%Y-%m-%d')] = \
                        data[args['field']][current_date.strftime('%Y-%m-%d')]
                current_date += pd.DateOffset(1)
            return {'symbol': symbol, 'field': args['field'], 'value': results}, 200
        else:
            abort(404, message='Symbol {} does not exists!'.format(symbol))
