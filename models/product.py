from app import db
from sqlalchemy.dialects.postgresql import JSON


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
