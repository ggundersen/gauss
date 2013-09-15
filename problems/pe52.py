"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02-05

Problem:
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order. Find the smallest positive integer,
x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    for n in xrange(1, 300000):
        is_perm = True
        for i in range(1,7):
            if g.is_permutation(n, n*i) == False:
                is_perm = False
                break
        if is_perm == True:
            return n