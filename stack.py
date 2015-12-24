from wsStackImpl import wsStack

class Stack(object):
    def __init__(self, type):
        # FIXME: Must be a better way to do this than string comparison
        if type == "wsStack":
            wsStack()
        else:
            raise NotImplementedError

