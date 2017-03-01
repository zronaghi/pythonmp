import random
import time
import multiprocessing
from multiprocessing import Pool
import numpy

def dot_product_mp(chunk):
    return numpy.dot (chunk[0], chunk[1])

lower = -1.0
upper = 1.0
size = 10000000
np = multiprocessing.cpu_count()
step = size/np

print "parallel numpy dot product on numpy arrays", np

for j in range(10):
    v1 = numpy.random.uniform(lower, upper, size)
    v2 = numpy.random.uniform(lower, upper, size)

    chunks = list()

    for i in range(0, size, step):
       chunks.append([v1[i:i+step], v2[i:i+step]])
    
    
    pool = Pool(processes=np)

    start = time.time()    
    count = sum(pool.map(dot_product_mp, chunks) )
   
   
    print j, time.time() - start, count
