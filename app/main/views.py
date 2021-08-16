from app.models import Category, Pitch
from app.main.forms import CategoryForm, PitchForm
from flask import render_template,redirect,url_for
from flask_login import login_required
from . import main
from .. import db


@main.route('/',methods=['GET','POST'])
def index():
    return render_template('maintemplates/index.html')


@main.route('/secret')
@login_required
def secret():
    return 'Only auth users are allowed'

@main.route('/biz')
def biz():
    return render_template('maintemplates/business_pitch.html')


@main.route('/addCategory',methods=['POST','GET'])
def addCategory():
    form=CategoryForm()
    if form.validate_on_submit():
        category=Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('maintemplates/addcategory.html',form=form)
@main.route('/addPitch',methods=['POST','GET'])
def addPitch():
    form=PitchForm()
    if form.validate_on_submit():
        pitch_body=Pitch(pitch_body=form.pitch_body.data)
        db.session.add(pitch_body)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('maintemplates/addpitch.html',form=form)