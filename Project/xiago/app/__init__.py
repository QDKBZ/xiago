from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_aqlalchemy import SQLALchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLALchemy()

def create_app(confog_name):
    app = Flask(__name__)
    app.config.from_object(config[confog_name])
    config[confog_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    return app