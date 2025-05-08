from flask import jsonify, request
from flask_restful import Resource
from app import db

from app.auth.models import Users
from app.auth.serde import UsersSchema


class Signupviews(Resource):

    def post(self):
        data=request.get_json()

        exist_username=Users.query.filter_by(username=data['username']).count()
        if exist_username:
            return jsonify({"message":"Username Already exist"})
        
        exist_email=Users.query.filter_by(email=data['email']).count()
        if exist_email:
            return jsonify({"message":"Email Already exist"})
        
        new=UsersSchema().load(data)
        print(new)
        print(data)
        new_data=Users(**new)
        db.session.add(new_data)
        db.session.commit()


        return jsonify({"message":"User Added successfull"})

    