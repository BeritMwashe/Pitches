from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from .  import db
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    pitches=db.relationship('Pitch',backref='owner',lazy='dynamic')
    
    
    def generate_confirmation_token(self,expiration=3600):
        s=Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})


    def confirm(self,token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token)
        except:
            return False
        if data.get('confirm')!=self.id:
            return False
        self.confirmed=True
        return True
        
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

class Pitch(db.Model):
    __tablename__='pitches'
    id=db.Column(db.Integer,primary_key=True)
    pitch_body=db.Column(db.String(64))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    categories_id =db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
        return '<Pitch %r>' % self.pitch_body


class Category(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))
    pitches = db.relationship("Pitch", backref="category",lazy='dynamic')



class Comments()