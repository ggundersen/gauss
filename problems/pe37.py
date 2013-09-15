"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-24

Problem:
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3. Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    result = []
    p = 23
    while len(result) < 11:
        if g.is_truncatable(p):
            result.append(p)
        p += 2
    return sum(result)