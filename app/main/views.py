from flask import render_template
from flask_login import login_required
from . import main



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