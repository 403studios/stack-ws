def get_config():
    # DEFAULTS
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = None
    STACK = 'LocalCollection'
    HTTP_AUTH_USERNAME = 'admin'
    HTTP_AUTH_PASSWORD = 'secret'

    try:
        with open('.env', 'r') as env_file:
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
