**Got a question?** Email me!

# stack-ws

An implementation of the stack data structure using RESTful web services.

This is a sample project for interviewee assignments.

Contents:
  - [Exercise Instructions](#exercise-instructions)
  - [Installation](#installation)
  - [Configuring](#configuring)
  - [Running](#running)
  - [Examples](#examples)
  - [Documentation](#documentation)

----------

### Exercise Instructions
This exercise is aimed towards learning about an interviewee's approach to exploratory testing. There is no right answer.

Great testers are skilled in careful observation, critical thinking, and possess a rich collection of tools, information, and resources.

Using the [session-based testing](https://en.wikipedia.org/wiki/Session-based_testing) methodology, you will complete several test sessions each lasting approximately 30 minutes. Keep in mind exploratory testing is not ad-hoc testing. Exploratory testing is simultaneous learning, test design, and test execution.

Remember, a big advantage to using session-based testing is flexibility. If you discover an oddity during your session, you may want to explore it further or use this information to form subsequent test charters.

The goal of each of these test sessions is outlined by its test charter. Test charters are a guideline for you to define your testing mission and to outline what kind of problems you want to look for.

You will be given one or more testing charters. You may also be asked to create some test charters of your own to execute.

Steps to complete:

1. Familiarize yourself with the project. Read documentation provided, review any technologies in use that you aren't familiar with, review open and recently-closed issues, review code, environment, etc. You should receive a demo of this project to demonstrate functionality. If you have not, please send me an email.

2. Create any required test charters. Once complete, set up a quick review session and present your test charters to the team.

3. Execute your test session. On a small-scale project like this, each test session should take less than 30 minutes. Larger projects will generally have a longer test session time. One of the disadvantages of session-based testing is reproducibility so be sure to gather evidence and take good notes to capture your observations as you're executing test sessions. You may be asked to try to reproduce your observations.

4. Once each your test session is complete, prepare a Test Session Report. The Test Session report should consist of the following sections:

  - Session charter
  - Session length
  - Task breakdown
  - Data files
  - Test notes
  - Issues
  - Bugs

  Further info about Test Session Reports can be found [Here](https://simonsaysnomore.wordpress.com/2014/08/19/session-based-test-layout-session-report/).

5. Once all test charters are complete, setup a debriefing session to review your findings and discuss your results.

**Important Note:** Don't be shy! Ask questions if you're unsure of what to do. The goal of this exercise is not to trick you or evaluate your psychic abilities. We both get more out of this exercise if you ask questions and provide feedback along the way.

Feel free to use anything you have been given and any tools at your disposal.

### Installation
This application has been tested using Ubuntu 14.04 LTS (Trusty Tahr) and MacOS 10.11 (El Capitan). All versions of Windows are unsupported - use at your own risk.

The following instructions will install system-wide dependencies. Therefore, [virtualenv](https://pypi.python.org/pypi/virtualenv) is strongly recommended. You will also need to use [git](https://git-scm.com) to clone the source repository.
    
1. Clone repo:

        $ git clone https://github.com/403studios/stack-ws
2. Run:

        $ python setup.py install

### Configuring
See [application_config.py](https://github.com/403studios/stack-ws/blob/master/src/stackapi/application_config.py) for a description of all configurable options.

### Running
All necessary dependencies will be installed during [Installation](#installation). To run:

    $ run_stack_app

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
API Documentation is automatically-generated at runtime. Documentation can be accessed at: `http://<host>:<port>/documentation`
