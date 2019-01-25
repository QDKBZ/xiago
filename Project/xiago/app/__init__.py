from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from app import models
# from app.models import db
from .main import settings, blue

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()



def create_app(version="default"):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    app.config.from_object(settings.config.get(version, 'default'))

    migrate = Migrate(app=app, db=models.db)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    app.register_blueprint(blue)
    models.db.init_app(app)
    migrate.init_app(app)

    return app