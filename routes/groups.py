from flask_restful import Resource


class GroupsEndpoint(Resource):
    @staticmethod
    def get():
        return {"foo": "bar"}


class GroupsIdEndpoint(Resource):
    @staticmethod
    def get(group_id):
        return {"id": str(group_id)}
