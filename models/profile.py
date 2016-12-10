from app import db
from sqlalchemy.dialects.postgresql import JSON


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
