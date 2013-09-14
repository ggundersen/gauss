'''
DESCRIPTION:
Project Euler, problem 36
Gregory Gundersen, 01/21/2013

PROBLEM:

SOLUTION:
872187
'''

import time
import gmath as g
s = time.time()

result = 0
for n in range(1, 1000000):
    if g.is_palindrome(n):
        n2 = g.base10_to_baseK(n, 2, [])
        if g.is_palindrome(n2):
            result += n

print result
print 'Time: ' + str(time.time() - s)
