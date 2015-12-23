from flask import Flask, request
from flask.ext.api import status
from stack import Stack

application = Flask(__name__)
application.config.from_pyfile('config.py')

# Stack objects container
wsStackList = []

@application.route("/")
def main():
    return "Hello World"

# Manage the list of stack objs
@application.route("/stack", methods = ['GET', 'POST'])
def stackMgr():
    if request.method == 'GET':
        for i in wsStackList:
            print i
        return str(wsStackList)
    elif request.method == 'POST':
        s = Stack()
        wsStackList.append(s)
        return str(wsStackList.index(s))

# Manage stack operations
@application.route("/stack/<int:id>", methods = ['GET', 'POST', 'DELETE'])
def stack(id):
    if request.method == 'GET':
        try:
            return str(wsStackList[id])
        except (IndexError, ValueError) as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR
    # Push to stack
    elif request.method == 'POST':
        try:
            wsStackList[id].push(request.get_data())
            return request.get_data()
        except (IndexError, ValueError) as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR
    # Pop from stack
    elif request.method == 'DELETE':
        try:
            return wsStackList[id].pop()
        except (IndexError, ValueError) as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR

# Retrieve stack size
@application.route("/stack/<int:id>/size", methods = ['GET'])
def stackSize(id):
    if request.method == 'GET':
        return str(wsStackList[id].size())

# Retrieve topmost element of stack
@application.route("/stack/<int:id>/peek", methods = ['GET'])
def stackPeek(id):
    if request.method == 'GET':
        try:
            return str(wsStackList[id].peek())
        except (IndexError, ValueError) as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR

# Clear the stack. Remove all elements.
@application.route("/stack/<int:id>/clear", methods = ['DELETE'])
def stackClear(id):
    if request.method == 'DELETE':
        try:
            return str(wsStackList[id].clear())
        except (IndexError, ValueError) as ie:
            return str(ie), status.HTTP_500_INTERNAL_SERVER_ERROR
        

if __name__ == "__main__":
    application.debug = application.config["DEBUG"]
    application.run(host=application.config["HOST"], port=application.config["PORT"])
