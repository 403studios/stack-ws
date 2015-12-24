from abc import ABCMeta, abstractmethod

class AbstractBaseStack(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def isEmpty(self):
        return

    @abstractmethod
    def push(self, item):
        '''Add item to the stack.'''
        return

    @abstractmethod
    def pop(self):
        '''Retrieve the topmost item and remove it from the stack.'''
        return

    @abstractmethod
    def peek(self):
        '''Retrieve the topmost item from the stack.'''
        return

    @abstractmethod
    def size(self):
        '''Retrieve the topmost item from the stack.'''
        return

    @abstractmethod
    def clear(self):
        '''Clear the stack. Remove all elements.'''
        return