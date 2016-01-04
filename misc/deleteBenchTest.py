#! /usr/bin/env python

'''
Simple Benchmark test to evaluate the performance of removing all elements from
a list using the assignment operator and using the del statement.
'''

import timeit

'''
Compare two samples and print the winner
'''
def findWinner(s1, s2, desc1="Sample 1", desc2="Sample 2"):
    if s1 < s2:
        print "Sample 1 wins! %s is faster." % (desc1)
    elif s2 < s1:
        print "Sample 2 wins! %s is faster." % (desc2)
    elif s1 == s2:
        # These are floats. Unlikely this will happen
        print "Sample 1 and Sample 2 are tied! %s and %s are equally fast." % \
            (desc1, desc2)
    else:
        # Something went wrong
        print "Cannot determine winner between %s and %s." % (desc1, desc2)

'''
Test setup method. Passed to the timeit constructor to initialize test
conditions
'''
setup = '''
numSamples = 10000
sampleSize = 1000
import random
import string
l = list()
print "numSamples = %s" % (numSamples)
print "sampleSize = %s" % (sampleSize)
for i in range(0,numSamples):
    l.append(''.join(random.choice(string.ascii_uppercase + string.digits)
        for _ in range(sampleSize)))
'''

'''
Test samples. Each test will execute one million times.
'''
t1 = timeit.Timer('l = []', setup=setup).timeit() # Use Assignment
t2 = timeit.Timer('del l[:]', setup=setup).timeit() # Use Delete

print "time to clear using assignment operator: {:>0f} seconds".format(t1)
print "time to clear using del statement: {:>14f} seconds".format(t2)
print
findWinner(t1, t2, "Assignment", "Delete")
