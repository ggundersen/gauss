'''
DESCRIPTION:
Project Euler, problem 49
Gregory Gundersen, 01/30/2013

PROBLEM:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

SOLUTION:
296962999629
'''

import time
import gmath as g
           
def main():
    
    pg =  g.gen_sieve_of_eratosthenes()
    p, primes = 1, []
        
    while p < 10000:
        p = pg.next()
        p2 = p + 3330
        p3 = p + 6660
        if g.isPrime(p2) and g.isPrime(p3):
            if g.is_permutation(p, p2) and g.is_permutation(p, p3):
                primes.append([str(p), str(p2), str(p3)])

    return ''.join(primes[1])

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
