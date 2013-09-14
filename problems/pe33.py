'''
DESCRIPTION:
Project Euler, problem 33
Gregory Gundersen, 02/14/2013

PROBLEM:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

SOLUTION:
Fractions: 16/64, 19/95, 26/65, 49/98
100
'''

import time
import gmath as g

def main():
    cf = []
    for n in range(10, 100):
        for d in range(n+1, 100):

            fr = float(n) / d
            n1, n2 = float(str(n)[0]), float(str(n)[1])
            d1, d2 = int(str(d)[0]), int(str(d)[1])
            
            if (d%10 and d1 and d2) != 0:
                if (n1 == d1 and fr == n2 / d2) or \
                   (n1 == d2 and fr == n2 / d1) or \
                   (n2 == d1 and fr == n1 / d2) or \
                   (n2 == d2 and fr == n1 / d1):
                    cf.append([n,d])

    num, dem = 1, 1
    for i in range(len(cf)):
        num *= cf[i][0]
        dem *= cf[i][1]
    gcd = g.get_gcd(dem, num)
    
    return dem / gcd

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
