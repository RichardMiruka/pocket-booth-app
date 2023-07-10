from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    friend = db.relationship('Friend', backref='user')
    def __init__(self, name):
        self.name = name

class Image(db.Model):
    __tablename__='images'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    friend = db.relationship('Friend', backref="images")

    def __init__(self, filename=None):
        self.filename = filename

class Friend(db.Model):
    __tablename__="friend"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))

    # user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('friends'))
    # friend = db.relationship('User', foreign_keys=[friend_id])
