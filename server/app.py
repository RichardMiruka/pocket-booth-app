from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return 'Welcome to the Pocket Booth App!'

# Route to post an image
@app.route('/images', methods=['POST'])
def post_image():
    data = request.get_json()
    filename = data.get('filename')

    if not filename:
        return jsonify({'error': 'Filename is required'}), 400

    image = Image(filename=filename)
    db.session.add(image)
    db.session.commit()

    return make_response(jsonify({'message': 'Image posted successfully'}), 201)

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
# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'name': user.name} for user in users]

    return jsonify(user_list), 200

# Route to get all friends for a given user
@app.route('/users/<int:user_id>/friends', methods=['GET'])
def get_user_friends(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    friends = [{'id': friend.id, 'name': friend.name} for friend in user.friends]

    return jsonify(friends), 200

if __name__ == '__main__':
    app.run()

