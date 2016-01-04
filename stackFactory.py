from localStack import LocalStack
from localCollection import LocalCollection

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
        elif factory == 'LocalCollection':
            return LocalCollectionFactory()
        raise NotImplementedError('Unknown Factory.')

'''
Concrete factory implmenetation for the Local Stack class.
'''
class LocalStackFactory(object):
    ''' Returns a new instance of the Local Stack class. '''
    def getStackFactory(self):
        return LocalStack()

'''
Concrete factory implementation for the Local Collection class.
'''
class LocalCollectionFactory(object):
    ''' Returns a new instance of the Local Collection class.'''
    def getStackFactory(self):
        return LocalCollection()
