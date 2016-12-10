import config
from routes.groups import GroupsEndpoint, GroupsIdEndpoint
from routes.interests import InterestsEndpoint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config.from_object(config.Config())
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api.add_resource(GroupsEndpoint, "/groups")
api.add_resource(GroupsIdEndpoint, "/groups/<int:group_id>")

api.add_resource(InterestsEndpoint, "/interests")

if __name__ == "__main__":
    app.run()
