import math

def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
# this is so much better isn't it?
