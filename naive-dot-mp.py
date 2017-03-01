import random
import time
import multiprocessing
from multiprocessing import Pool

def random_vector(lower = -1.0, upper = 1.0, size = 10000000):
    return [ random.uniform(lower, upper) for i in range(size) ]

def dot_product_mp(chunk):
    product = 0.0
    for i in range(len(chunk[0])):
        product += chunk[0][i] * chunk[1][i]
    return product

lower = -1.0
upper = 1.0
size = 10000000
np = multiprocessing.cpu_count()
step = size/np

print "parallel dot product on Python lists", np

for j in range(10):
    v1 = random_vector(lower, upper, size)
    v2 = random_vector(lower, upper, size)

    chunks = list()

    for i in range(0, size, step):
       chunks.append([v1[i:i+step], v2[i:i+step]])
    
    pool = Pool(processes=np)

    start = time.time()
    count = sum(pool.map(dot_product_mp, chunks) )
   
   
    print j, time.time() - start, count
