from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from sqlalchemy.dialects.postgresql import JSON
from flask_restful import Api
import os

# setup
app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)
db = SQLAlchemy(app)

# models
class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image_url = db.Column(db.String())
    email_list = db.Column(JSON)

    def __init__(self, name, image_url, email_list):
        self.name = name
        self.image_url = image_url
        self.email_list = email_list

    def __repr__(self):
        return "<id {}>".format(self.id)

class Interest(db.Model):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<id {}>".format(self.id)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    cost = db.Column(db.String())
    url = db.Column(db.String())
    image_url = db.Column(db.String())
    tags = db.Column(JSON)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<id {}>".format(self.id)

class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    phone = db.Column(db.String())
    interests = db.Column(JSON)

    def __init__(self, name, phone, interests):
        self.name = name
        self.phone = phone
        self.interests = interests

    def __repr__(self):
        return "<id {}>".format(self.id)

# routes
class GroupsEndpoint(Resource):
    @staticmethod
    def get():
        return {"foo": "bar"}

class GroupsIdEndpoint(Resource):
    @staticmethod
    def get(group_id):
        return {"id": str(group_id)}

class InterestsEndpoint(Resource):
    @staticmethod
    def get():
        return [
            {"name": "Sport"},
            {"name": "Clothes"},
            {"name": "Ramzi"}
        ]

api.add_resource(GroupsEndpoint, "/groups")
api.add_resource(GroupsIdEndpoint, "/groups/<int:group_id>")
api.add_resource(InterestsEndpoint, "/interests")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
