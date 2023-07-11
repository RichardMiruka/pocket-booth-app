from app import app, db
from models import User, Image, Friend

with app.app_context():
    db.create_all()

    # Create users
    user1 = User(name='Richard')
    user2 = User(name='Sharoun')
    user3 = User(name='Rebecca')

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Create images for user1
    image1 = Image(filename='image1.jpg')
    image2 = Image(filename='image2.jpg')

    image1.user = user1
    image2.user = user1

    db.session.add_all([image1, image2])
    db.session.commit()

    # Create friends
    friend1 = Friend(user=user1, friend=user2)
    friend2 = Friend(user=user1, friend=user3)
    friend3 = Friend(user=user2, friend=user3)

    db.session.add_all([friend1, friend2, friend3])
    db.session.commit()


    
    