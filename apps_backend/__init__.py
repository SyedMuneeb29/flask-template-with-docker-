from flask import Flask # used for routing
# from flask_sqlalchemy import SQLAlchemy # used dealing with data base , running queries etc
from flask_marshmallow import Marshmallow # is helps in serializing data into json from sql data
from flask_restful import Api  # it helps you writte route in class way

app = Flask(__name__) #routing with app

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
# db = SQLAlchemy(app)
ma = Marshmallow(app)


from . views import *
