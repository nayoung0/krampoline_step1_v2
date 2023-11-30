from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import path

# db = SQLAlchemy()
DB_NAME = 'krampoline_step1_v2.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'semicircle_secret_key hollimoly guacamole roly poly'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///krampoline_step1_v2.db'
    # db.init_app(app)
    
    from .views import views

    app.register_blueprint(views, url_prefix='/api')
    
    # from .models import User, Map
    # create_database(app)
    
    return app

# def create_database(app):
#     if not path.exists('server/' + DB_NAME):
#         db.create_all(app=app)
#         print(">>>>> Create DB")