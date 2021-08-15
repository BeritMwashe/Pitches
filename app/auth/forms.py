

from ..models import User
from tokenize import String
from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,Length,Regexp,EqualTo





class LoginForm(Form):
    email=StringField('Email',validators=[Required(),Email()])
    password=PasswordField('Password',validators=[Required()])
    remember_me=BooleanField('Keep me logged in')
    submit=SubmitField('Login In')

class Registrationform(Form):
    email=StringField('email',validators=[Required(),Email(),Length(1,64)])
    username=StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
'Usernames must have only letters, '
'numbers, dots or underscores')])
    password=PasswordField('Password',validators=[Required(),EqualTo('password2',message='Password must match')])
    password2=PasswordField('Confirm Password',validators=[Required()])
    submit=SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email alredy registered')
            

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username exixts')