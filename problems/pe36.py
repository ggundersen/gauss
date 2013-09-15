"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-21

Problem:
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    result = 0
    for n in range(1, 1000000):
        if g.is_palindromic_number(n):
            n2 = g.base10_to_baseK(n, 2, [])
            if g.is_palindromic_number(n2):
                result += n
    return result