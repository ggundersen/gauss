"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02-05

Problem:
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube. Find the
smallest cube for which exactly five permutations of its digits are cube.

Solution:
The key (Pythonic) observation is that a sorted string is an efficient check
for permutations.
----------------------------------------------------------------------------"""

       
def main():
    
    cubes = {}
    num_perms = 5
    
    for i in range(345, 1000000):
        c = i*i*i
        v = ''.join(sorted(str(c)))
        if cubes.has_key(v):
            cubes[v].append(c)
        else:
            cubes[v] = [c]
        if len(cubes[v]) == num_perms:
            return cubes[v][0]