from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
 

class user(db.metadatasodel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
def __init__(self, name):
    self.name = name

class Image(db.Model)
def __init__ (self, filename=None) :
    pass

class Friends :
# Class for storing friends list and their details
 pass