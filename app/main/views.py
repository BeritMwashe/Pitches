from os import name
from app.models import Category, Pitch, User
from app.main.forms import CategoryForm, PitchForm
from flask import render_template,redirect,url_for,request
from flask_login import current_user, login_required
from . import main
from .. import db


@main.route('/',methods=['GET','POST'])
def index():
    categories=Category.query.all()
    return render_template('maintemplates/index.html',categories=categories)



@main.route('/viewbizpitch/<name>',methods=['GET','POST'])
def biz(name):
    #pitch=Pitch.query.all()
    pitch=Pitch.query.join(Category).filter(Category.name==name).all()
    return render_template('maintemplates/business_pitch.html',pitch=pitch)


@main.route('/addCategory',methods=['POST','GET'])
def addCategory():
    form=CategoryForm()
    if form.validate_on_submit():
        category=Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('maintemplates/addcategory.html',form=form)



@main.route('/addComent',methods=['POST','GET'])
def addComment():
    form=CommentsForm()
    if form.validate_on_submit():
        comment=Comment(name=form.name.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('maintemplates/addcomment.html',form=form)
@main.route('/addPitch',methods=['POST','GET'])
@login_required
def addPitch():
    categories=Category.query.all()
    

    form=PitchForm()
    form.category.choices=[(cat.id,cat.name ) for cat in categories]
    if form.validate_on_submit():
        user=current_user.username
        category=Category.query.filter_by(id=form.category.data).first()
        print(category)
        print(current_user._get_current_object())
        pitch=Pitch(owner=current_user._get_current_object(),pitch_body=form.pitch_body.data,category=category)
          
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('maintemplates/addpitch.html',form=form)
