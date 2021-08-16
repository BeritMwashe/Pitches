
from unicodedata import category

from flask_login import current_user
from ..models import User

from flask_wtf import Form
from wtforms import SelectField,StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Email,Length,Regexp,EqualTo

class CategoryForm(Form):
    name=StringField('Category',validators=[Required()])
    submit=SubmitField('Submit Category')


class PitchForm(Form):
    pitch_body=StringField('Pitch',validators=[Required()])
    category=SelectField('Select category',choices=[])
    # owner=User.query.filter_by(email=current_user.email).first()
    submit=SubmitField('Submit')



class CommentsForm(Form):
    comment=StringField('Comment',validators=[Required()])
    




