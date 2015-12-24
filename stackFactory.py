from stack import Stack

class AbstractStackFactory(object):
    @staticmethod
    def getStackFactory(factory):
        if factory == 'Stack':
            return StackFactory()
        raise NotImplementedError('Unknown Factory.')

class StackFactory(object):
    def getStackFactory(self):
        return Stack()
