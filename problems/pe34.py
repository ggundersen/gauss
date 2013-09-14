'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time, math
s = time.time()

# 9! is the maximum value for any one digit
# 9! < 7 digits
# Upper bound is 9! * 7
limit = 7 * math.factorial(9)

ans = 0
for n in range(3, limit):
    l = list(str(n))
    if n == sum(math.factorial(int(i)) for i in l):
        print n
        ans += n

print ans
print 'Time: ' + str(time.time() - s)
