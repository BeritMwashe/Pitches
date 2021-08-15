from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from .  import db


class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    @property
    def password(self):
        '''password ensures password is write only not read'''
        raise AttributeError('password is not readbale atribute')

    @password.setter
    def password(self,password):
        '''after pass set calls generatepass that writes the hashed pasword to password_hash field pass cant be recovered once hashed'''
        self.password_hash=generate_password_hash(password)


    def verify_password(self,password):
        '''checks if password hashed === with password'''
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Roles(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.column(db.String(64))
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


