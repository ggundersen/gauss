"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02

Problem:
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime. There are thirteen such primes
below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many circular
primes are there below one million?

Solution:
My solution is trivial, but there is an optimization: the prime cannot contain
an even digit. Clearly one of those digits would appear at the end of the
number, making that rotation not prime. Optimization needs to happen at the
gmath level.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    gen =  g.gen_sieve_of_eratosthenes()
    p = 0
    result = 1 # gen.next() skips 2

    while p < 1000000:
        p = gen.next()
        if g.is_circular_prime(p):
            result += 1
    return result