from setuptools import setup
from os.path import abspath, dirname, join

CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, 'src', 'stackapi', 'version.py')) as f:
    exec(f.read())
    VERSION = get_version()

setup(
    name='stackapi',
    version=VERSION,
    description='An implementation of a stack using RESTful web services',
    author='403Studios',
    author_email='403studiosca@gmail.com',
    package_dir={'': 'src'},
    packages=['stackapi'],
    url='https://github.com/403studios/stack-ws',
    dependency_links=[
        'https://github.com/mitsuhiko/flask/tarball/master',
        'https://github.com/acoomans/flask-autodoc/tarball/master',
    ],
    setup_requires=[
        'flask',
    ],
    install_requires=[
        'flask',
        'flask-autodoc',
    ],
    scripts=[
        'src/bin/run_stack_app'
    ],
    zip_safe=False
)
