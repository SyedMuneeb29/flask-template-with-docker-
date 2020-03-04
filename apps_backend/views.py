from . import api
from flask_restful import Resource

class IndexView(Resource) :
    def get(self) :
        return "Main Index"

api.add_resource(IndexView , "/api/index")
