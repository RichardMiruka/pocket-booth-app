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

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

#     def __init__(self, name):
#         self.name = name

# class Image(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.String(100), nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     user = db.relationship('User', backref=db.backref('images', cascade='all, delete-orphan'))

#     def __init__(self, filename=None):
#         self.filename = filename

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

if __name__ == '__main__':
    app.run()

