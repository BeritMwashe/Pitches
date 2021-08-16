
from ..models import User

from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,Length,Regexp,EqualTo

class CategoryForm(Form):
    name=StringField('Category',validators=[Required()])
    submit=SubmitField('Submit Category')


class PitchForm(Form):
    pitch_body=StringField('Pitch',validators=[Required()])
    submit=SubmitField('Submit')




