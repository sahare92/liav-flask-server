import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

USER_TO_PASSWORD = {
    'sahar': '123456',
    'liav': '123',
    'lhabin': '422542',
}


class Login(Resource):
    # def get(self):
    #     return {}

    def post(self):
        """
        Post will receive user credentials, and will return True response if they're ok
        Input: {'username': <username>, 'password': <password>}
        """
        response = {}
        request_data = json.loads(request.get_data())
        print(str(request_data))

        # TODO: implement this part (add login validation here)
        request_username = request_data['username']
        request_password = request_data['password']

        if USER_TO_PASSWORD[request_username] == request_password:
            response = {'response': 'ok'}
        else:
            response = {'response': 'unauthorized'}
        # TODO: END of your code

        return response


api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(debug=True, port=3000)

