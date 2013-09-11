"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-20

Problem:
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    hi = 20162
    ab_nums = []
    ab_hash = {}
    result = 0

    for n in range(12, hi):
        if g.is_abundant(n):
            ab_nums.append(n)
            ab_hash[n] = n
    for S in range(1, hi):
        flag = True
        for n in ab_nums:
            if ab_hash.get(S-n) != None:
                flag = False
                break
        if flag: result += S
    return result