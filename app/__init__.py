from flask_bootstrap import Bootstrap
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from config import config_options


bootstrap=Bootstrap()
mail=Mail()
db=SQLAlchemy()



def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    



    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app