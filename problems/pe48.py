'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
'''

import time
s = time.time()
a = 0

for n in range(1,1001):
    a += n**n

print str(a)[len(str(a))-10:]
print 'Time: ' + str(time.time() - s)
