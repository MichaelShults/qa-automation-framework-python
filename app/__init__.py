import os
from flask import Flask
from flask_appbuilder import AppBuilder
from .views import FooView
from .database import db



def create_app():
    app = Flask(__name__)
    with app.app_context():

        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
        app.config['SECRET_KEY'] = 'secretkey'

        db.init_app(app)
        db.create_all()

        appbuilder = AppBuilder(app, db.session)
        appbuilder.add_view(FooView, "Foos",icon="fa-folder-open-o")
    return app
