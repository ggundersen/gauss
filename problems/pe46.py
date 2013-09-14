'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import time, gmath
s = time.time()

def isGoldbach(c):
    g = gmath.genPrimes()
    for p in range(c):
        prime = g.next()
        for s in range(c):
            if c == (prime + 2*(s**2)):
                return True
    return False

c = gmath.genCompositesOdd()
cTemp = c.next()
while isGoldbach(cTemp):
    cTemp = c.next()

print cTemp
print 'Time: ' + str(time.time() - s)
