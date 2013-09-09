'''
DESCRIPTION:
Project Euler, problem 15
Gregory Gundersen, 1/15/2013

PROBLEM:
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20x20 grid?

RESOLUTION:
My first attempt to consider the problem combinatorially.
Since backtracking is prohibited, we can assign a value to "right" and "down"
and every unique solution should have the same sum. If right = 1 and down = 0,
then the number of paths is the same as the number of unique permutations
of a 40 digit number, half 0s and half 1s, that equals 20.
This solution was computationally expensive but provided me with the initial values for various triangles.
After playing around algebraically, I stumbled upon a pattern of triangular numbers.
This led to a general solution using figurate numbers.
I enjoyed this problem because it reinforced the idea that mathematics ties seemingly disparate problems together.
'''

import time
import gmath as g
s = time.time()

def getPaths(M):
    result = 1
    for num in range(1, M+1):
        result += g.getFigurate(num, M)
    return result

print getPaths(20)
print 'Time: ' + str(time.time() - s)
