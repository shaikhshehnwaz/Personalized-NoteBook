

from functools import wraps

from flask import g, jsonify, request
from app import app
import jwt


def token_required(f):
    @wraps(f)
    def decorators(*args,**kwargs):
        token=request.cookies.get('token')

        if not token:
            return jsonify({"message":"Missing token"})
        
        try:
            data=jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
            g.user_id=data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({"message":"Token expire"})
        except jwt.InvalidTokenError:
            return jsonify({"message":"Invalid token"})  

        return f(*args,**kwargs)

    return decorators  

