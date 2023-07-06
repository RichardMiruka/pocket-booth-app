#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User, Image, Friend

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to the Pocket Booth App!'

# Route to post an image
@app.route('/images', methods=['POST'])
def post_image():
    data = request.json
    filename = data.get('filename')

    if not filename:
        return jsonify({'error': 'Filename is required'}), 400

    image = Image(filename=filename)
    db.session.add(image)
    db.session.commit()

    return jsonify({'message': 'Image posted successfully'}), 201

# Route to delete an image
@app.route('/images/<int:image_id>', methods=['DELETE'])
def delete_image(image_id):
    image = Image.query.get(image_id)

    if not image:
        return jsonify({'error': 'Image not found'}), 404

    db.session.delete(image)
    db.session.commit()

    return jsonify({'message': 'Image deleted successfully'}), 200

# Route to get all images
@app.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    image_list = [{'id': image.id, 'filename': image.filename} for image in images]

    return jsonify(image_list), 200

# Route to post a comment on an image
@app.route('/images/<int:image_id>/comments', methods=['POST'])
def post_comment(image_id):
    image = Image.query.get(image_id)

    if not image:
        return jsonify({'error': 'Image not found'}), 404

    data = request.json
    comment = data.get('comment')

    if not comment:
        return jsonify({'error': 'Comment is required'}), 400

    image.comments.append(comment)
    db.session.commit()

    return jsonify({'message': 'Comment posted successfully'}), 201

# Route to like an image
@app.route('/images/<int:image_id>/like', methods=['POST'])
def like_image(image_id):
    image = Image.query.get(image_id)

    if not image:
        return jsonify({'error': 'Image not found'}), 404

    image.likes += 1
    db.session.commit()

    return jsonify({'message': 'Image liked successfully'}), 200

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'name': user.name} for user in users]

    return jsonify(user_list), 200

# Route to create a user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    app.run()

