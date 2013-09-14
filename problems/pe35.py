'''
DESCRIPTION:
Project Euler, problem 35
Gregory Gundersen, ../../2013

PROBLEM:
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

SOLUTION:
Trivial; the sieve is critical to optimization, though
Interesting optimization: the prime cannot contain 0, 2, 4, 6, 8
Clearly one of those digits would appear at the end of the number, making
that rotation not prime
55
'''

import time
import gmath as g

def main():

    pg =  g.gen_sieve_of_eratosthenes()
    p = 0
    c = 1 # pg.next() skips 2

    while p < 1000000:
        p = pg.next()
        if g.is_circular_prime(p):
            c += 1
    return c

s = time.time()
main()
print 'Time: ' + str(time.time() - s)
