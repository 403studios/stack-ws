''' stackFactory '''
from stack import Stack

''' AbstractStackFactory '''
class AbstractStackFactory(object):
    ''' This is the AbstractStackFactory class. '''
    @staticmethod
    def getStackFactory(factory):
        ''' Returns a new instance of the Stack Factory. '''
        if factory == 'Stack':
            return StackFactory()
        raise NotImplementedError('Unknown Factory.')

''' StackFactory '''
class StackFactory(object):
    ''' This is the StackFactory class. '''
    def getStackFactory(self):
        ''' Returns a new instance of the Stack implementation. '''
        return Stack()
