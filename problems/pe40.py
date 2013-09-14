'''
DESCRIPTION:
Project Euler, problem 40
Gregory Gundersen, 01/24/2013

PROBLEM:
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

SOLUTION:
210
'''

import time
import gmath as g

def main():
    L = ['0']
    for i in range(1, 200000):
        L.append(str(i))
    L = ''.join(L)
    return int(L[1]) * int(L[10]) * int(L[100]) * int(L[1000]) * int(L[10000]) * int(L[100000]) * int(L[1000000])

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
