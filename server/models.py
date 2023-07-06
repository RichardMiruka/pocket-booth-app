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

class Friends :
# Class for storing friends list and their details
 pass