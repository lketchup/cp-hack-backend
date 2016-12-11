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
            'first_name': 'Ramzi',
            'last_name': 'Mohawk',
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
                'img_url': 'https://i.imgur.com/kBAgkZw.jpg',
                'price': 3.99,
                'description': '3D printed ramzi action figure!',
                'owner': {
                    'name': 'Myer',
                    'logo_url': 'http://myersupplier.myer.com.au/images/myer_logo_large.jpg',
                }
            },
            {
                'id': 2,
                'name': 'RIDLEYS Games Room Poker Set',
                'url': 'http://www.myer.com.au/shop/mystore/giftorium-stocking-fillers/ridleys-344815300-344818720--1',
                'img_url': 'http://www.myer.com.au/wcsstore/MyerCatalogAssetStore/images/65/652/5233/141/8/344815300_344818720/344815300/344815300_zm_1.jpg',
                'price': 99.95,
                'description': 'This Texas Hold\'em Poker Set includes poker chips, dealer button, two card decks and instructions. Beautifully giftboxed in graphic Games room packaging.\n    Contents:\n    200 x poker chips\n    1 x dealer button\n    2 x decks of 52 cards\n    Instructions',
                'owner': {
                    'name': 'Myer',
                    'logo_url': 'http://myersupplier.myer.com.au/images/myer_logo_large.jpg',
                }
            },
            {
                'id': 3,
                'name': 'NANOBLOCK Unicorn',
                'url': 'http://www.myer.com.au/shop/mystore/giftorium-stocking-fillers/nanoblock-nanoblock-unicorn',
                'img_url': 'http://www.myer.com.au/wcsstore/MyerCatalogAssetStore/images/65/652/5233/141/5/404726590_404727940/404726590_zm_1.jpg',
                'price': 12.95,
                'description': 'Nanoblock is a micro sized building block from Japan. Piece together these challenging models, to create amazingly detailed building   block master pieces. Totally addictive building block fun for ages 12+',
                'owner': {
                    'name': 'Myer',
                    'logo_url': 'http://myersupplier.myer.com.au/images/myer_logo_large.jpg',
                }
            },
            {
                'id': 4,
                'name': 'Kindle Paperwhite eReader Black',
                'url': 'http://www.officeworks.com.au/shop/officeworks/p/kindle-paperwhite-ereader-black-amkindpapw',
                'img_url': 'http://s3-ap-southeast-2.amazonaws.com/wc-prod-pim/JPEG_1000x1000/AMKINDPAPW_.jpg',
                'price': 169.99,
                'description': 'This Kindle Paperwhite eReader is perfect for anyone who takes their reading on the go. It features an inbuilt, adjustable light that ensures the screen looks like real paper in any environment.\n    This Kindle has a 300 ppi display which ensures that it feels like you are reading from real paper.\n    The Kindle is anti-glare so you can take your reading out into the sunlight.\n    The inbuilt, adjustable light will let you find the right brightness depending on the time of day.\n    This Kindle has access to over a million books and can download another book in under 60 seconds.\n    This is a 3rd generation Kindle.\n    It has a long battery life that can last up to 2 weeks off 1 charge.\n    It comes with a 12 month manufacturer\'s warranty.\n    The eReader is a stylish black colour.',
                'owner': {
                    'name': 'officeworks',
                    'logo_url': 'https://lh3.googleusercontent.com/-WvD-PEnLv3A/UpK1QmFkbTI/AAAAAAAAAJk/7PWYnBX-fbo/s299-no/youtube_profile.png',
                }
            },
            {
                'id': 5,
                'name': 'Kindle Oasis eReader Black',
                'url': 'http://www.officeworks.com.au/shop/officeworks/p/kindle-oasis-ereader-black-amkinoasis',
                'img_url': '',
                'price': 449.99,
                'description': 'The Kindle Oasis eReader has a super thin and light design, making it incredibly comfortable to hold while reading. This Kindle has a long lasting battery, easy to use page turning buttons and a built in light, making it perfect for taking on the go.\n This Kindle has a 300 ppi display, which makes it feel like you are reading from paper.',
                'owner': {
                    'name': 'officeworks',
                    'logo_url': 'https://lh3.googleusercontent.com/-WvD-PEnLv3A/UpK1QmFkbTI/AAAAAAAAAJk/7PWYnBX-fbo/s299-no/youtube_profile.png',
                }
            }
        ]
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
