**Got a question?** Email me!

# stack-ws

---
An implementation of the stack data structure using RESTful web services.

This is a sample project for interviewee assignments.

---
  - [Instructions](#instructions)
  - [Installation](#installation)
  - [Configuring](#configuring)
  - [Running](#running)
  - [Examples](#examples)
  - [Documentation](#documentation)

---
### Instructions

### Installation
This application has been tested using Ubuntu 14.04 LTS (Trusty Tahr) and MacOS 10.11 (El Capitan).

The following instructions will install system-wide dependencies. Therefore, [virtualenv](https://pypi.python.org/pypi/virtualenv) is strongly recommended. You will also need to use [git](https://git-scm.com) to clone the source repository.
    
1. Clone repo:

        git clone https://github.com/403studios/stack-ws
2. Run:

        python setup.py install

### Configuring
See [application_config.py](https://github.com/403studios/stack-ws/blob/master/src/stackapi/application_config.py) for a description of all configurable options.

### Running
All necessary dependencies will be installed during [Installation](#installation). To run:

    run_stack_app

### Examples
The following examples are provided for convenience. These examples do not represent all available features. See the API [Documentation](#documentation) for a comprehensive list of all capabilities.

#### Using [cURL](http://curl.haxx.se)
###### Create a new stack:

    $ curl -u '<username>:<password>' -d '' http://<host>:<port>/stack
    0

If this call is successful, a stack id will be returned. This can be used for subsequent operations on this stack.

###### Push data to a stack:
Push the string 'foo' to the stack.

    $ curl -u '<username>:<password>' -d 'foo' http://<host>:<port>/stack/0
    foo

###### Read the stack:

    $ curl -u '<username>:<password>' http://<host>:<port>/stack/0
    deque(['foo'])

###### Read the size of the stack:

    $ curl -u '<username>:<password>' http://<host>:<port>/stack/0/size
    1

###### Pop data from the stack:

    $ curl -u '<username>:<password>' -X Delete http://<host>:<port>/stack/0
    foo

### Documentation
Documentation can be accessed at: `http://<host>:<port>/documentation`
