from app import db
from sqlalchemy.dialects.postgresql import JSON


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
