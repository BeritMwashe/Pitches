from .forms import LoginForm
from flask import render_template
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    return render_template('authtemplates/login.html',form=form)