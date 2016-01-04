'''
Flask debugging features
'''
DEBUG = True

'''
Flask host argument
'''
HOST = '0.0.0.0'

'''
Flask port argument. None is Flask's default port (5000)
'''
PORT = None

'''
Stack implementation to use.
Valid choices:
              'LocalStack' : Python built-in list data type.
              'LocalCollection' : Python built-in collection data type.
                                  Collections are a high-performance list-like
                                  container with fast appends and pops.
'''
STACK_FACTORY = 'LocalCollection'