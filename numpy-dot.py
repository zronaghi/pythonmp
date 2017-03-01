import random
import time
import numpy

lower = -1.0
upper = 1.0
size = 10000000

print "numpy dot product on numpy arrays"

for i in range(10):
    v1 = numpy.random.uniform(lower, upper, size)
    v2 = numpy.random.uniform(lower, upper, size)
    start = time.time()
    result = numpy.dot(v1, v2)
    print i, time.time() - start, result
