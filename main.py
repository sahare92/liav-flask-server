import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import cross_origin, CORS

app = Flask(__name__)
CORS(app)

USER_TO_PASSWORD = {
    'sahar': '123456',
    'liav': '123',
    'lhabin': '422542',
}


@app.route('/login', methods=['POST'])
def login():
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


if __name__ == '__main__':
    app.run(debug=True, port=3005)

