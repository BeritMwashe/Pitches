from tabnanny import check
from werkzeug.security import generate_password_hash,check_password_hash
from ..app import db


class User(db.Model):
    password_hash=db.Column(db.String(128))


    def password(self):
        '''password ensures password is write only not read'''
        raise AttributeError('password is not readbale atribute')


    def password(self,password):
        '''after pass set calls generatepass that writes the hashed pasword to password_hash field pass cant be recovered once hashed'''
        self.password_hash=generate_password_hash(password)


    def verify_password(self,password):
        '''checks if password hashed === with password'''
        return check_password_hash(self.password_hash,password)

