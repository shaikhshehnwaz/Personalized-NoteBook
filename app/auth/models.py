from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)
    _password=db.Column(db.String(256),nullable=False)
    notes=db.relationship("Notes",backref='users',cascade='all,delete')

    @property
    def password(self):
      """Reading the plaintext is not allowed"""
      raise AttributeError("Cannot read password")

    @password.setter
    def password(self,password):
        """Converting password into hash password"""
        self._password = generate_password_hash(password)

    def verify_password(self,password):
        """Checking hash password using check_password_hash"""
        return check_password_hash(self._password,password)