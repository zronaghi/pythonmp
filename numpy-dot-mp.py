import random
import time
import sys
import multiprocessing
from multiprocessing import Pool
import numpy

def dot_product_mp_new(chunk):
    global v1, v2, step
    start = time.time()
    product = numpy.dot(v1[chunk:chunk+step], v2[chunk:chunk+step])
    end = time.time()
    #print 'inner time is', end-start
    return product

lower = -1.0
upper = 1.0
size = int(sys.argv[1])
np = int(sys.argv[2])
print 'Array size is', size
print '# of procs is', np
step = size/np

print "parallel numpy dot product on numpy arrays", np
#v1 = numpy.random.uniform(lower, upper, size)
#v2 = numpy.random.uniform(lower, upper, size)

#start = time.time()
#result = numpy.dot(v1, v2)
#print "Warm up", time.time() - start

for j in range(4):
    v1 = numpy.random.uniform(lower, upper, size)
    v2 = numpy.random.uniform(lower, upper, size)

    chunks = list()

    for i in range(0, size, step):
        chunks.append(i)
    
    pool = Pool(processes=np)

    start = time.time()    
    count = sum(pool.map(dot_product_mp_new, chunks) )
    end = time.time()
   
    print j, end - start
