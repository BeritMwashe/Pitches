from os import abort, name
from app.models import Category, Comment, DisLike, Like, Pitch, User
from app.main.forms import CategoryForm, CommentsForm, PitchForm
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
    for pitches in pitch:
         print(pitches.id)
         
    #     com=[]
    #     comments=Comment.query.join(Pitch).filter(Pitch.id==pitches.id).all()
    #     com.append(comments)
    #     print(comments)
    # likes=Like.getlikes()
    # likes=Like.getlikes(id)
    return render_template('maintemplates/business_pitch.html',pitch=pitch,)


@main.route('/addCategory',methods=['POST','GET'])
@login_required
def addCategory():
    form=CategoryForm()
    if form.validate_on_submit():
        category=Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('maintemplates/addcategory.html',form=form)



@main.route('/addComent/<pitch>',methods=['POST','GET'])
@login_required
def addComment(pitch):
    form=CommentsForm()
    pitch=Pitch.query.filter_by(id=pitch).first()
    if form.validate_on_submit():
        comment=Comment(comment=form.comment.data,pitch=pitch)
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
@main.route('/like/<int:id>',methods=['POST','GET'])
@login_required
def like(id):
    

    pitch_id=Pitch.query.filter_by(id=id).first()
    name=Pitch.query.filter_by(id=id).first()
    user_like_exists=Like.getlikes(id)
    print(user_like_exists)
    if len(user_like_exists)==0:
        new_like=Like(user=current_user._get_current_object(),liker=pitch_id)
        new_like.save()
    else:
            for uel in user_like_exists:
                if uel.user_id==current_user.id:
                    print('exists')
                    break
                else:
                    print('difrent')
                    new_like=Like(user=current_user._get_current_object(),liker=pitch_id)
                    new_like.save()
                    print(new_like)

    likes=Like.getlikes(id)
    return redirect(url_for('main.biz', name=name.category.name))
   
    
@main.route('/dislikes/<int:id>',methods=['POST','GET'])
@login_required
def dislikes(id):
    

    pitch_id=Pitch.query.filter_by(id=id).first()
    name=Pitch.query.filter_by(id=id).first()
    user_like_exists=DisLike.getdislikes(id)
    print(user_like_exists)
    if len(user_like_exists)==0:
        new_like=DisLike(dislikeuser=current_user._get_current_object(),disliked=pitch_id)
        new_like.save()
    else:
            for uel in user_like_exists:
                if uel.user_id==current_user.id:
                    print('exists')
                    break
                else:
                    print('difrent')
                    new_like=DisLike(dislikeuser=current_user._get_current_object(),disliked=pitch_id)
                    new_like.save()
                    print(new_like)

    dislikes=DisLike.getdislikes(id)
    return redirect(url_for('main.biz', name=name.category.name))
   
    
@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()


    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user)