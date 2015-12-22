from flask import Flask, request
from flask.ext.api import status
from stack import Stack

application = Flask(__name__)

s = Stack()

@application.route("/")
def main():
    return "Hello World"

@application.route("/stack", methods = ['GET', 'POST', 'DELETE'])
def stack():
    if request.method == 'GET':
        try:
            return s.pop(), status.HTTP_200_OK
        except IndexError as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR
    elif request.method == 'POST':
        try:
            s.push(request.get_data())
            return request.get_data(), status.HTTP_200_OK
        except:
            pass

    elif request.method == 'DELETE':
        try:
            s.clear()
            return "", status.HTTP_200_OK
        except:
            pass

    else:
        return "", status.HTTP_405_METHOD_NOT_ALLOWED

@application.route("/stack/size", methods = ['GET'])
def size():
    if request.method == 'GET':
        return str(s.size()), status.HTTP_200_OK

@application.route("/stack/peek", methods = ['GET'])
def peek():
    if request.method == 'GET':
        try:
            return s.peek(), status.HTTP_200_OK
        except IndexError as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
