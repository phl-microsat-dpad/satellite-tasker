from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from imagery_request import views, models, endpoints

api = Api(app)
api.add_resource(endpoints.Orders, '/api/order', endpoint='api.order')
