from flask import Flask, render_template, config
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from .main import main

# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
from .models import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/project?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    #app.config.from_object(config[confog_name])
    #config[confog_name].init_app(app)

    # bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)
    app.debug = True
    app.register_blueprint(main)
    return app