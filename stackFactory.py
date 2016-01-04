from stack import Stack

'''
AbstractStackFactory is effectively a generic interface to concrete factories 
of various implementations of the stack datastype.
'''
class AbstractStackFactory(object):
    ''' Returns a new instance of the Stack Factory. '''
    @staticmethod
    def getStackFactory(factory):
        if factory == 'Stack':
            return StackFactory()
        raise NotImplementedError('Unknown Factory.')

'''
Concrete factory implmenetation for the Stack class.
'''
class StackFactory(object):
    ''' Returns a new instance of the Stack implementation. '''
    def getStackFactory(self):
        return Stack()
