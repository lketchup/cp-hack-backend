import os
from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/groups/<int:index>/<int:size>/', methods=['GET', 'POST'])
def groups(index, size):
    if request.method == 'GET':
        return jsonify([
            {
                'id': 1,
                'name': 'Ramzi\'s',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            },
            {
                'id': 2,
                'name': 'Ramzi\'s',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            },
            {
                'id': 3,
                'name': 'Ramzi\'s',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            },
            {
                'id': 4,
                'name': 'Ramzi\'s',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            },
            {
                'id': 5,
                'name': 'Ramzi\'s',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            },
        ])
    elif request.method == 'POST':
        return jsonify(request.get_json())

@app.route('/groups/<int:id>/<int:index>/<int:size>/', methods=['GET', 'PUT'])
def group(id, index, size):
    if request.method == 'GET':
        return jsonify({
            'id': id,
            'name': 'Ramzi\'s',
            'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
            'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            'profiles': [
                {
                    'id': 1,
                    'name': 'Ramzi',
                    'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                },
                {
                    'id': 2,
                    'name': 'Pat',
                    'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
                },
            ]
        })
    elif request.method == 'PUT':
        return jsonify(dict({'id': id}, **request.get_json()))

@app.route('/profiles/', methods=['POST'])
def profiles():
    return jsonify(request.get_json())

@app.route('/profiles/<int:id>/<int:index>/<int:size>/', methods=['GET', 'POST'])
def profile(id, index, size):
    if request.method == 'GET':
        return jsonify({
            'id': id,
            'name': 'Ramzi',
            'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
            'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            'interests': [
                'arab fighting',
                'not coding',
                'entering data into unresponsive excel',
            ],
            'products': [
                {
                    'id': 1,
                    'name': 'Ramzi action figure',
                    'url': 'http://google.com/',
                    'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                    'price': 3.99,
                    'description': '3D printed ramzi action figure!',
                },
                {
                    'id': 2,
                    'name': 'Ramzi action figure',
                    'url': 'http://google.com/',
                    'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                    'price': 3.99,
                    'description': '3D printed ramzi action figure!',
                },
                {
                    'id': 3,
                    'name': 'Ramzi action figure',
                    'url': 'http://google.com/',
                    'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                    'price': 3.99,
                    'description': '3D printed ramzi action figure!',
                },
                {
                    'id': 4,
                    'name': 'Ramzi action figure',
                    'url': 'http://google.com/',
                    'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                    'price': 3.99,
                    'description': '3D printed ramzi action figure!',
                },
                {
                    'id': 5,
                    'name': 'Ramzi action figure',
                    'url': 'http://google.com/',
                    'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                    'price': 3.99,
                    'description': '3D printed ramzi action figure!',
                }
            ]
        })
    elif request.method == 'POST':
        return jsonify(dict({'id': id}, **request.get_json()))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
