"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02-05

Problem:
The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 * 7
    15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:
    644 = 2^2 * 7 * 23
    645 = 3 * 5 * 43
    646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
----------------------------------------------------------------------------"""

import lib.gmath as g
      

def main():
    
    factors = []
    for i in range(150000):
        factors.append(g.get_prime_factors(i))

    for i in range(1, len(factors)-4):
        if len(set(factors[i])) == 4 and len(set(factors[i+1])) == 4 and\
            len(set(factors[i+2])) == 4 and len(set(factors[i+3])) == 4:
            if set(factors[i]) & set(factors[i+1]) & set(factors[i+2]) &\
                set(factors[i+3]) == set([]):
                return i