import email
import os


from flask_login import current_user, login_required, login_user, logout_user
from ..models import User
from .forms import LoginForm, Registrationform
from flask import render_template,redirect,request,url_for,flash
from . import auth
from .. import db
from ..email import send_email


@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            # return redirect(request.args.get('next') or url_for('main.index'))
            return redirect(url_for('main.index'))
       
    return render_template('authtemplates/login.html',form=form)







@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



# @auth.route('/confirm')
# @login_required
# def resend_confirmation():
#     token = current_user.generate_confirmation_token()
#     send_email('authtemplates/email/confirm',
#     'Confirm Your Account', user, token=token)
#     flash('A new confirmation email has been sent to you by email.')
#     return redirect(url_for('main.index'))


@auth.route('register',methods=['GET','POST'])
def register():
    print (os.environ.get("EMAIL_USER")) 
    '''registers user,save to db, add to this session'''
    form=Registrationform()
    if form.validate_on_submit():
        user=User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        send_email(user.email,'Confirm your mail','authtemplates/email/confirm',user=user)

        print(user)
        return redirect(url_for('auth.login'))
    return render_template('authtemplates/register.html',form=form)



