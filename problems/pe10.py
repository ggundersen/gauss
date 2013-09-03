"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Solution:
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():
    sum = 2    # begin at 2, then iterate over only odd numbers
    for i in range(3, 2000001, 2):
        if g.is_prime(i):
            sum += i
    return sum