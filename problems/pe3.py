"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-09-03
2013-01


Problem:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Solution:
The algorithm is trivial, but there are two optimizations that can be made.
First, we do not need to search higher than n^(1/2). Second, by using the Sieve
of Eratosthenes, we can efficiently and lazily load prime numbers rather than
iterating over integers, checking for primality, and then checking for
divisibility. The latter optimization reduced runtime by approximately tenfold.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    result = 0
    n = 600851475143
    limit = int(n**0.5)
    gen = g.gen_sieve_of_eratosthenes()
    p = gen.next()

    while p < limit:
    	if n % p == 0:
    		result = p
    	p = gen.next()
    return result