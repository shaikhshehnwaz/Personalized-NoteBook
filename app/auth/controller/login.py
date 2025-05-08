


from flask import jsonify, make_response, request
from flask_restful import Resource
from datetime import datetime, timedelta
import jwt
from app.auth.models import Users
from app import app

class LoginView(Resource):

    def post(self):
     
      data1=request.get_json()

      user=Users.query.filter_by(username=data1['username']).first()
      if not user:
         return "Username is Invalid",401
      
    #   exist_password=Users.query.filter_by(verify_password=data['username']).first()

      if not user.verify_password(data1['password']):
         return "Password is Invalid",401
      
      expire_at=datetime.utcnow() + timedelta(minutes=20)

      token=jwt.encode(
         {
            "user_id" : user.id , 
            "email":user.email,
            "exp":expire_at 
         },
         app.config['SECRET_KEY'],
         algorithm='HS256'
      )

      response=make_response(jsonify({"message":"User login successful"}))
      response.set_cookie('token',token,expires=expire_at)

      return response

    