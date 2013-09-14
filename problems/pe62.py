'''
DESCRIPTION:
Project Euler, problem 62
Gregory Gundersen, 02/05/2013

PROBLEM:
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.

SOLUTION:
Similar to my get_permutations function, the key observation is that a sorted string is an efficient check for permutations.
127035954683
'''

import time
       
def main():
    
    cubes = {}
    num_perms = 5
    
    for i in xrange(345, 1000000):
        c = i*i*i
        v = ''.join(sorted(str(c)))
        if cubes.has_key(v):
            cubes[v].append(c)
        else:
            cubes[v] = [c]
        if len(cubes[v]) == num_perms:
            return cubes[v][0]
        
s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
