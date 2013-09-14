'''
DESCRIPTION:
Project Euler, problem 52
Gregory Gundersen, 02/05/2013

PROBLEM:
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

SOLUTION:
142857
'''

import time
import gmath as g

def main():
    for n in xrange(1, 300000):
        flag = True
        for i in range(1,7):
            if g.is_permutation(n, n*i) == False:
                flag = False
                break
        if flag == True:
            return n

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
