from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/note'
app.config['SECRET_KEY'] = "notes"

db=SQLAlchemy(app)

from app.auth.controller import auth_blueprint

app.register_blueprint(auth_blueprint,url_prefix=f"/api/{auth_blueprint.url_prefix}")

from app.md.controller import md_blueprint

app.register_blueprint(md_blueprint,url_prefix=f"/api/{md_blueprint.url_prefix}")