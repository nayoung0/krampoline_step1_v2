from server import db
from datetime import datetime


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    # maps = db.relationship('Map')
        
    def __repr__(self):
        return f"<User('{self.id}', '{self.username}')>"

class Map(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    start_at = db.Column(db.String(50))
    end_at = db.Column(db.String(50))
    season = db.Column(db.String(50))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
    # content = db.Column(db.String(2000))
    # lo_1_visit = db.Column(db.Boolean, default=False, nullable=False)
    # lo_2_visit = db.Column(db)