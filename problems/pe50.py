"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02-07

Problem:
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
----------------------------------------------------------------------------"""

import lib.gmath as g


def get_primes(limit):
    gen = g.gen_sieve_of_eratosthenes()
    primes = []
    while True:
        p = gen.next()
        if p <= limit:
            primes.append(p)
        else:
            break
    return primes


def get_sums(limit):
    primes = get_primes(limit)
    sums = [0]
    sm = 0
    for i in range(len(primes)):
        sm += primes[i]
        if sm <= limit: # this is the key to runtime success
            sums.append(sm)
    return sums

def main():
    limit = 1000000
    sums = get_sums(limit)
    t = 1 # num of terms
    result = 1 # max prime
    for i in range(len(sums)):
        for j in range(len(sums)):
            n = sums[j] - sums[i] # sum
            l = j-i # len
            if g.is_prime(n) and l > t and n <= limit:
                t = l
                result = n
    return result