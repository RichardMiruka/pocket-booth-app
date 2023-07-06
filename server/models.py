from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
def __init__(self, name):
    self.name = name

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    
def __init__ (self, filename=None) :
    self.filename = filename

class Friends(db.Model):
    id = db.column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship('User', foreign_keys=[user_id],backref=db.backref('friends'))
    friend = db.relationship('User', foreign_keys=[friend_id])
# Class for storing friends list and their details
 pass