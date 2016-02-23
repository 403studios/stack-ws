from setuptools import setup
from os.path import abspath, dirname, join
from sys import version_info as python_version

assert python_version >= (2, 7), \
    "Please upgrade to the latest version of python 2.7, "\
    "your version of python might not work"
assert python_version < (3, 0), \
    "Please use the latest version of python 2.7, "\
    "this project is not compatible with python 3"

CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, 'stackapi', 'version.py')) as f:
    exec(f.read())
    VERSION = get_version()

setup(
    name='stackapi',
    version=VERSION,
    description='An implementation of a stack using RESTful web services',
    author='403Studios',
    author_email='403studiosca@gmail.com',
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
    tests_require=[
        'flask',
        'flask-autodoc',
    ],
    test_suite="tests",
    scripts=[
        'bin/run_stack_app'
    ],
    zip_safe=False
)
