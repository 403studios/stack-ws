from setuptools import setup
from os.path import abspath, dirname, join

CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, 'src', 'stackapi', 'version.py')) as f:
    exec(f.read())
    VERSION = get_version()

setup(
    name='stackapi',
    version=VERSION,
    decription='A test project for interview purpose',
    author='403Studios',
    author_email='rob.mcleod@gmail.com',
    package_dir={'': 'src'},
    packages=['stackapi'],
    url='https://github.com/403studios/stack-ws',
    install_requires=[
        'flask',
        'flask-api',
        'flask-autodoc',
    ],
    scripts=[
        'src/bin/run_stack_app'
    ]
)