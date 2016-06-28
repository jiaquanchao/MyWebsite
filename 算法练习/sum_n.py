import numpy as np
import random

def sum_n(n, A):
    if n > 0: return sum_n(n-1, A) + A[n]

if __name__ == '__main__':
    a = list(map(lambda x: random.randint(0, 6), [y for y in range(10)]))
    print (a)
    sum_n(4, a)
