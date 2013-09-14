'''
DESCRIPTION:
Project Euler, problem 41
Gregory Gundersen, 01/24/2013

PROBLEM:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

SOLUTION:
Number theory: upper bound can be greatly reduced by analysis
Computation: search top to bottom, only odd
'''

import time
import gmath as g

def main():
    for n in range(7654321, 1, -2):
        if g.is_pandigital(n) and g.isPrime(n):
                return n
    return None

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
