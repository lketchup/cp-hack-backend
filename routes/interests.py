from flask_restful import Resource


class InterestsEndpoint(Resource):
    @staticmethod
    def get():
        return [
            {"name": "Sport"},
            {"name": "Clothes"},
            {"name": "Ramzi"}
        ]