from itertools import count, islice
import math

def is_pow_two(x):
    ln = math.log(x, 2)
    return ln == math.floor(ln)

print(list(islice(filter(is_pow_two, count(1000)),0,3)))
