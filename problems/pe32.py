"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-24

Problem:
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital. The product 7254 is unusual, as the identity, 39 * 186 =
7254, containing multiplicand, multiplier, and product is 1 through 9
pandigital. Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():
    result = []
    for x in range(1, 60):
        for y in range(1, 2000):
            p = x*y
            z = str(x) + str(y) + str(p)
            if g.is_pandigital(z) and len(z) == 9 and p not in result:
                result.append(p)
    return sum(result)