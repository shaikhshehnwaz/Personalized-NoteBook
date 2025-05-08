from flask import jsonify, make_response, request
from flask_restful import Resource

from app.auth.models import Users

class LogoutView(Resource):
    def get(self):   
        response=make_response(jsonify({"message":"Logout successful"}))
        response.delete_cookie('token')
        return response
    
