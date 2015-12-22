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
            return s.pop()
        except IndexError as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR
    elif request.method == 'POST':
        try:
            s.push(request.get_data())
            return request.get_data()
        except:
            pass
    elif request.method == 'DELETE':
        try:
            s.clear()
            return
        except:
            pass
    else:
        return "", status.HTTP_405_METHOD_NOT_ALLOWED

@application.route("/stack/size", methods = ['GET'])
def size():
    if request.method == 'GET':
        return str(s.size())

@application.route("/stack/peek", methods = ['GET'])
def peek():
    if request.method == 'GET':
        try:
            return s.peek()
        except IndexError as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
