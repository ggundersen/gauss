'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

(see 'euler_p13_numbers.txt')
'''

import time, fileinput
s = time.time()
total = 0

for line in fileinput.input(['pe13_number.txt']):
    total += int(line)

print str(total)[:10]
print 'Time: ' + str(time.time() - s)
