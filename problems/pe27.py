'''
DESCRIPTION:
Project Euler, problem 27
Gregory Gundersen, 02/12/2013

PROBLEM:
Euler published the remarkable quadratic formula: n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form: n^2 + a*n + b, where |a| < 1000 and |b| < 1000
where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |4| = 4, find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

SOLUTION:

'''

import time, operator
import gmath as g

s = time.time()

def is_prime_quadratic(n, a, b):
    if g.isPrime(n**2 + a*n + b):
        return True
    return False

max_c = 0
max_m = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        c = 0
        n = 0
        m = a*b
        while is_prime_quadratic(n, a, b):
            c += 1
            n += 1
        if c > max_c:
            max_c = c
            max_m = m

print max_c
print max_m
print time.time() - s










