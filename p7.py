'''
Project euler Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math
from itertools import islice

def findPrimeUnderLimit(limit):
    primes = range(2,limit)

    for n in primes:
        factors = range(n,limit,n)
        for x in factors[1:]:
            print(n)
            if x in primes:
                primes.remove(x)
    return(primes)

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x%2==0:
        return False
    return all(x % i for i in range(3,int(math.sqrt(x)+1),2))

def prime_gen(limit,start=2,):
    x = start
    while x<=limit:
        if is_prime(x):
            yield x
        x += 1



