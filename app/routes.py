from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Flask backend is running!', 200

@main.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask API'}, 200
