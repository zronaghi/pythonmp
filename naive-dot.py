import random
import time

def random_vector(lower = -1.0, upper = 1.0, size = 10000000):
    return [ random.uniform(lower, upper) for i in range(size) ]

def dot_product_1(v1, v2):
    """This is like 3x slower than dot_product_2, cool."""
    return sum(a * b for (a, b) in zip(v1, v2))

def dot_product_2(v1, v2):
    total = 0.0
    n = len(v1)
    for i in range(n):
        total += v1[i] * v2[i]
    return total

lower = -1.0
upper = 1.0
size = 10000000

print "regular dot product on Python lists"

for i in range(10):
    v1 = random_vector(lower, upper, size)
    v2 = random_vector(lower, upper, size)
    start = time.time()
    result = dot_product_2(v1, v2)
    print i, time.time() - start, result
