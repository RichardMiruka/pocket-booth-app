#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, User,Image, Friend

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return 'Welcome to the Pocket Booth App'


if __name__ == '__main__':
    app.run()

