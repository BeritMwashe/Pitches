import email
from urllib import request

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


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        print('confirmed')
    else:
        print('Invalid confirmation')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5]!='auth.':
        return redirect(url_for('auth.unconfirmed'))



@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous():
        return redirect('main.index')
        return render_template('authtemplates/unconfirmed.html')




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email('authtemplates/email/confirm',
    'Confirm Your Account', user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


@auth.route('register',methods=['GET','POST'])
def register():
    '''registers user,save to db, add to this session'''
    form=Registrationform()
    if form.validate_on_submit():
        user=User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token=user.generate_confirmation_token()
        send_email(user.email,'confirm Your Account','authtemplates/email/confirm',user=user,token=token)

        print(user)
        return redirect(url_for('auth.login'))
    return render_template('authtemplates/register.html',form=form)



