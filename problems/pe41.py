"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-24

Problem:
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

Solution:
There are two optimizations to searching this space. First, note that the upper
bound is 7654321--8 and 9 digit numbers are always divisible by 3. For example:

    1+2+3+4+5+6+7+8 = 36

Second, search only odd numbers from high to low.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    for n in range(7654321, 1, -2):
        if g.is_pandigital(n) and g.is_prime(n):
        	return n
    return None