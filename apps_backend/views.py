# used for generating responses :

from . import api
from flask_restful import Resource
from .controllers import *


class IndexView(Resource) :
    def get(self) :
        return "HelloWorld"


api.add_resource(CountryView , "/api/country")
