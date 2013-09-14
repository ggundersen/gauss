'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
'''

import time
s = time.time()

''' Ingest and process data '''
with open('PE67_triangle.txt') as f: tempTri = f.read().splitlines()
f.close()
tri = [row.split(' ') for row in tempTri]
for row in tri: row[:] = map(int, row[:])

''' update second-to-last nodes '''
def updateNodes(tri):
    L = len(tri)-1
    for node in range(len(tri[L-1])):
        tri[L-1][node] = max(tri[L-1][node] + tri[L][node], tri[L-1][node] + tri[L][node + 1])
    return tri

''' truncate triangle '''
def updateTriangle(tri):
    return tri[:len(tri)-1]

for row in range(len(tri)-1):
    updateNodes(tri)
    tri = updateTriangle(tri)

print tri
print 'Time: ' + str(time.time() - s)
