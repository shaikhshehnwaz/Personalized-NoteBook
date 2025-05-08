from flask_restful import Api
from flask import Blueprint
from app.auth.controller.login import LoginView
from app.auth.controller.logout import LogoutView
from app.auth.controller.signup import Signupviews

auth_blueprint=Blueprint("auth",__name__,url_prefix="/auth")
api=Api(auth_blueprint)

api.add_resource(Signupviews,"/signup")
api.add_resource(LoginView,"/login")
api.add_resource(LogoutView,"/logout")
