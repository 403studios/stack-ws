from localStack import LocalStack

'''
AbstractStackFactory is effectively a generic interface to concrete factories 
of various implementations of the stack datastype.
'''
class AbstractStackFactory(object):
    ''' Returns a new instance of the Stack Factory. '''
    @staticmethod
    def getStackFactory(factory):
        if factory == 'LocalStack':
            return LocalStackFactory()
        raise NotImplementedError('Unknown Factory.')

'''
Concrete factory implmenetation for the Local Stack class.
'''
class LocalStackFactory(object):
    ''' Returns a new instance of the Local Stack implementation. '''
    def getStackFactory(self):
        return LocalStack()
