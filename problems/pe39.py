'''
DESCRIPTION:
Project Euler, problem 39
Gregory Gundersen, 01/26/2013

PROBLEM:
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?

SOLUTION:
840
'''

import time
import gmath as g

s = time.time()

results = {}
for p in range(2, 1000, 2):
    t = g.get_pythagorean_triples(p)
    results[p] = len(t)
print max(results, key=results.get)

print 'Time: ' + str(time.time() - s)
