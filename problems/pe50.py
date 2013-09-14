'''
DESCRIPTION:
Project Euler, problem 50
Gregory Gundersen, 02/07/2013

PROBLEM:
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

SOLUTION:
997651
'''

import time
import gmath as g

# Generate primes
def gen_primes(lim):
    pg = g.gen_sieve_of_eratosthenes()
    primes = []
    while True:
        p = pg.next()
        if p <= lim:
            primes.append(p)
        else:
            break
    return primes

# Calc all possible sums
def get_sums(lim):
    primes = gen_primes(lim)
    sums = [0]
    sm = 0
    for i in range(len(primes)):
        sm += primes[i]
        if sm <= lim: # this is the key to runtime success
            sums.append(sm)
    return sums

def main():
    lim = 1000000
    sums = get_sums(lim)
    t = 1 # num of terms
    mp = 1 # max prime
    for i in range(len(sums)):
        for j in range(len(sums)):
            n = sums[j] - sums[i] # sum
            l = j-i # len
            if g.isPrime(n) and l > t and n <= lim:
                t = l
                mp = n
    return mp

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
