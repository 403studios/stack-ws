'''
Initial implementation from:
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html

With modification by Rob McLeod (rob.mcleod@gmail.com)
2015-12-24
    - Add clear method to clear all elements from the stack
'''
from abstractStack import AbstractStack

''' LocalStack implementation using a list as a backing datatype.'''
class LocalStack(AbstractStack):
    ''' Constructor '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
