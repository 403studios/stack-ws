"""
Flask debugging features.
"""
DEBUG = True

"""
Flask host argument.
"""
HOST = '127.0.0.1'

"""
Flask port argument. None is Flask's default port (5000).
"""
PORT = None

"""
Stack implementation to use.
Valid choices:
              'LocalStack' : Python built-in list data type.
              'LocalCollection' : Python built-in collection data type.
                                  Collections are a high-performance list-like
                                  container with fast appends and pops.
"""
STACK = 'LocalCollection'

"""
HTTP Basic auth username and password. Only a single username/password
combination is supported.
"""
HTTP_AUTH_USERNAME = 'admin'
HTTP_AUTH_PASSWORD = 'secret'


def get_config():
    try:
        with open('application_config.json', 'r') as env_file:
            import json
            config = json.load(env_file)
            env_file.close()
    except IOError:
        config = []

    return {
        "DEBUG": config.get('DEBUG') if 'DEBUG' in config else DEBUG,
        "HOST": config.get('HOST') if 'HOST' in config else HOST,
        "PORT": config.get('PORT') if 'PORT' in config else PORT,
        "STACK": config.get('STACK') if 'STACK' in config else STACK,
        "HTTP_AUTH_USERNAME": config.get('HTTP_AUTH_USERNAME') if 'HTTP_AUTH_USERNAME' in config else HTTP_AUTH_USERNAME,
        "HTTP_AUTH_PASSWORD": config.get('HTTP_AUTH_PASSWORD') if 'HTTP_AUTH_PASSWORD' in config else HTTP_AUTH_PASSWORD,
    }
