from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME = 'krampoline.db'

app = Flask(__name__)
db = SQLAlchemy(app)

def create_app():
    app.config['SECRET_KEY'] = 'semicircle_secret_key hollimoly guacamole roly poly'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    from server.views import views

    app.register_blueprint(views, url_prefix='/api')
    
    from server.models import User, Map
    create_database(app)
    
    return app



def create_database(app):
    if not path.exists('server' + DB_NAME):
        db.create_all()
        print(">>>>> Create DB")