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
                'name': 'Friends',
                'avatar_url': 'https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/15135732_10101446617309743_203228652896447949_n.jpg?oh=4d7590b8d61b0587ba398b581e556a7f&oe=58EF493D',
                'hero_url': 'https://s-media-cache-ak0.pinimg.com/originals/99/81/71/9981717f0ff14e7e8e2a6027574634d8.jpg',
            },
            {
                'id': 2,
                'name': 'Ramzi\'s',
                'avatar_url': 'https://scontent.xx.fbcdn.net/v/t1.0-0/p206x206/11350415_1440268869608793_9140529562314918683_n.jpg?oh=d7f1ace6794f0654abf62d608508c134&oe=58B9C840',
                'hero_url': 'http://www.getawayresort.com.au/wp-content/uploads/2012/06/bg_beach4.jpg?x74530',
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
                'last_name': 'Hossari',
                'avatar_url': 'https://i.imgur.com/8HWjERr.jpg',
            },
            {
                'id': 2,
                'first_name': 'Zac',
                'last_name': 'Love',
                'avatar_url': 'https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/15135732_10101446617309743_203228652896447949_n.jpg?oh=4d7590b8d61b0587ba398b581e556a7f&oe=58EF493D',
            },
            {
                'id': 3,
                'first_name': 'Lachlan',
                'last_name': 'Parker',
                'avatar_url': 'https://scontent.xx.fbcdn.net/v/t1.0-9/15799_10151377632902658_310185242_n.jpg?oh=00ad321714269bfce8a699afdf656faf&oe=58F9914D',
            },
            {
                'id': 4,
                'first_name': 'John',
                'last_name': 'Le',
                'avatar_url': 'https://scontent.xx.fbcdn.net/v/t1.0-0/p206x206/11350415_1440268869608793_9140529562314918683_n.jpg?oh=d7f1ace6794f0654abf62d608508c134&oe=58B9C840',
            },
        ]
    )

@app.route('/groups/<string:token>/<int:id>/', methods=['GET', 'PUT'])
def group(token, id):
    if request.method == 'GET':
        return jsonify({
            'id': 1,
            'name': 'Friends',
            'avatar_url': 'https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/15135732_10101446617309743_203228652896447949_n.jpg?oh=4d7590b8d61b0587ba398b581e556a7f&oe=58EF493D',
            'hero_url': 'https://s-media-cache-ak0.pinimg.com/originals/99/81/71/9981717f0ff14e7e8e2a6027574634d8.jpg',
        },)
    elif request.method == 'PUT':
        return jsonify(dict({'id': id}, **request.get_json()))

@app.route('/profiles/<string:token>/', methods=['POST'])
def profiles(token):
    return jsonify(request.get_json())

@app.route('/profiles/<string:token>/<int:id>/', methods=['GET', 'POST'])
def profile(token, id):
    if request.method == 'GET':
        return jsonify(
        {
            'id': 1,
            'first_name': 'Ramzi',
            'last_name': 'Hossari',
            'avatar_url': 'https://i.imgur.com/8HWjERr.jpg',
            'hero_url': 'http://www.getawayresort.com.au/wp-content/uploads/2012/06/bg_beach4.jpg?x74530',
            'email': 'ramzi',
            'interests': [
                'programming',
                'gaming',
                'board games',
                'dogs',
            ]
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
                'description': 'This Texas Hold\'em Poker Set includes poker chips, dealer button, two card decks and instructions. Beautifully giftboxed in graphic Games room packaging.\nContents:\n200 x poker chips\n1 x dealer button\n2 x decks of 52 cards\nInstructions',
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
                'description': 'This Kindle Paperwhite eReader is perfect for anyone who takes their reading on the go. It features an inbuilt, adjustable light that ensures the screen looks like real paper in any environment.',
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
                'description': 'The Kindle Oasis eReader has a super thin and light design, making it incredibly comfortable to hold while reading. This Kindle has a long lasting battery, easy to use page turning buttons and a built in light, making it perfect for taking on the go.',
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
