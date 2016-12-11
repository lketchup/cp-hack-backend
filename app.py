import os
from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/groups/<string:token>/<int:index>/<int:size>/', methods=['GET', 'POST'])
def groups(token, index, size):
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

@app.route('/groups/<string:token>/<int:id>/<int:index>/<int:size>/', methods=['GET'])
def group_profiles(token, id, index, size):
    return jsonify(
        [
            {
                'id': 1,
                'first_name': 'Ramzi',
                'last_name': 'Mohawk',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
            },
            {
                'id': 2,
                'first_name': 'Pat',
                'last_name': 'NoMohawk',
                'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
            },
        ]
    )

@app.route('/groups/<string:token>/<int:id>/', methods=['GET', 'PUT'])
def group(token, id):
    if request.method == 'GET':
        return jsonify({
            'id': id,
            'name': 'Ramzi\'s',
            'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
            'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
        })
    elif request.method == 'PUT':
        return jsonify(dict({'id': id}, **request.get_json()))

@app.route('/profiles/<string:token>/', methods=['POST'])
def profiles(token):
    return jsonify(request.get_json())

@app.route('/profiles/<string:token>/<int:id>/', methods=['GET', 'POST'])
def profile(token, id):
    if request.method == 'GET':
        return jsonify({
            'id': id,
            'name': 'Ramzi',
            'avatar_url': 'https://avatars1.githubusercontent.com/u/9994172?v=3&s=40',
            'hero_url': 'http://flask.pocoo.org/docs/0.11/_images/debugger.png',
            'email': 'ramzi',
            'interests': [
                'arab fighting',
                'not coding',
                'entering data into unresponsive excel',
            ],
        })
    elif request.method == 'POST':
        return jsonify(dict({'id': id}, **request.get_json()))

@app.route('/products/<string:token>/<int:profile_id>/<int:index>/<int:count>/', methods=['GET'])
def products(token, profile_id, index, count):
    return jsonify(
        [
            {
                'id': 1,
                'name': 'Ramzi action figure',
                'url': 'http://google.com/',
                'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                'price': 3.99,
                'description': '3D printed ramzi action figure!',
                'owner': {
                    'name': 'Target',
                    'logo_url': 'https://astridrodriguez.files.wordpress.com/2013/05/target-logo.png',
                }
            },
            {
                'id': 2,
                'name': 'Ramzi action figure',
                'url': 'http://google.com/',
                'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                'price': 3.99,
                'description': '3D printed ramzi action figure!',
                'owner': {
                    'name': 'Target',
                    'logo_url': 'https://astridrodriguez.files.wordpress.com/2013/05/target-logo.png',
                }
            },
            {
                'id': 3,
                'name': 'Ramzi action figure',
                'url': 'http://google.com/',
                'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                'price': 3.99,
                'description': '3D printed ramzi action figure!',
                'owner': {
                    'name': 'Target',
                    'logo_url': 'https://astridrodriguez.files.wordpress.com/2013/05/target-logo.png',
                }
            },
            {
                'id': 4,
                'name': 'Ramzi action figure',
                'url': 'http://google.com/',
                'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                'price': 3.99,
                'description': '3D printed ramzi action figure!',
                'owner': {
                    'name': 'Target',
                    'logo_url': 'https://astridrodriguez.files.wordpress.com/2013/05/target-logo.png',
                }
            },
            {
                'id': 5,
                'name': 'Ramzi action figure',
                'url': 'http://google.com/',
                'img_url': 'http://flask.pocoo.org/docs/0.11/_static/flask.png',
                'price': 3.99,
                'description': '3D printed ramzi action figure!',
                'owner': {
                    'name': 'Target',
                    'logo_url': 'https://astridrodriguez.files.wordpress.com/2013/05/target-logo.png',
                }
            }
        ]
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
