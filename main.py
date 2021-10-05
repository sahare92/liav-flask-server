import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

USERS = {
    'sahar': {},
    'liav': {},
    'lhabin': {},
}


class Login(Resource):
    def get(self):
        return {}

    def post(self):
        # TODO: implement this part (add login validation here)
        response = {}

        request_data = request.get_data()

        print(str(request_data))

        return response


api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
