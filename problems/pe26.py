"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-27

Problem:
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 0.5
1/3	= 0.(3)
1/4	= 0.25
1/5	= 0.2
1/6	= 0.1(6)
1/7	= 0.(142857)
1/8	= 0.125
1/9	= 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle. Find the value of d < 1000 for
which 1/d contains the longest recurring cycle in its decimal fraction part.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    # get primes less than 1000
    # remove 2 & 5, which are coprime with 10
    gen = g.gen_primes()
    L = []
    max_order = 0
    result = 0
    p = 1
    
    while p < 996:
        p = gen.next()
        L.append(p)
    L = L[3:]

    for p in L:
        temp_order = g.get_multiplicative_order(10, p)
        if temp_order > max_order:
            max_order = temp_order
            result = p

    return result