from flask import Flask, render_template
from flask_restful import Api

from api.resources.stock import Stock
from api.resources.user import User
from api.resources.trade import Trade


app = Flask(__name__)
api = Api(app)

api.add_resource(Stock, '/api/stocks/<string:symbol>')
api.add_resource(User, '/api/users/<string:uid>')
api.add_resource(Trade, '/api/trades/<string:tid>')


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
