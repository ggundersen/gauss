"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-26

PROBLEM:
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

    results = {}
    for p in range(2, 1000, 2):
        t = g.get_pythagorean_triples(p)
        results[p] = len(t)
    return max(results, key=results.get)