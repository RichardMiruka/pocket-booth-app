from app import app, db
from models import User, Image, Friend

with app.app_context():
    db.create_all()
    
    #Create a User
    user = User(name='Rebecca')
    db.session.add(user)
    db.session.commit()
    
    #Create an image associated with the User
    #and save it to disk (in this case as testimage12345678
    image = Image(filename='Rebecca.jpg')
    image.user = user
    db.session.add(image)
    db.session.commit()
    
    