'''
DESCRIPTION:
Project Euler, problem 43
Gregory Gundersen, ../../2013

PROBLEM:
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property. Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on.
In this way, we note the following:

d_2 * d_3 * d_4  =406 is divisible by 2
d_3 * d_4 * d_5  =063 is divisible by 3
d_4 * 5_d * d_6  =635 is divisible by 5
d_5 * d_6 * d_7  =357 is divisible by 7
d_6 * d_7 * d_8  =572 is divisible by 11
d_7 * d_8 * d_9  =728 is divisible by 13
d_8 * d_9 * d_10 =289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

SOLUTION:
Construct the solution backwards
The number has to equal 45

2  - begins at 100 - k2
3  - begins at 102 - k3
5  - begins at 100 - k5
7  - begins at 105 - k7
11 - begins at 110 - k11
13 - begins at 104 - k13
17 - begins at 102 - k17

16695334890
'''

import time

k2, k3, k5, k7, k11, k13, k17 = [], [], [] ,[] ,[] ,[], []

def k_append(k, n):
    if len(set(str(n))) == 3:
        k.append(str(n))
    if len(str(n)) == 2 and len(set(str(n))) == 2:
        k.append('0' + str(n))

def add_missing_digit(sn):
    digits = '0123456789'
    for d in digits:
        if d not in sn:
            return int(d+sn)

def main():

    for i in range(2, 999, 2):
        k_append(k2, i)
    for i in range(3, 999, 3):
        k_append(k3, i)
    for i in range(5, 999, 5):
        k_append(k5, i)
    for i in range(7, 999, 7):
        k_append(k7, i)
    for i in range(11, 999, 11):
        k_append(k11, i)
    for i in range(13, 999, 13):
        k_append(k13, i)
    for i in range(17, 999, 17):
        k_append(k17, i)

    results = {}
    for a in k2:
        for b in k3:
            if a[1] == b[0] and a[2] == b[1]:
                for c in k5:
                    if b[1] == c[0] and b[2] == c[1]:
                        for d in k7:
                            if c[1] == d[0] and c[2] == d[1]:
                                for e in k11:
                                    if d[1] == e[0] and d[2] == e[1]:
                                        for f in k13:
                                            if e[1] == f[0] and e[2] == f[1]:
                                                for g in k17:
                                                    if f[1] == g[0] and f[2] == g[1]:
                                                        sn = a+b[2]+c[2]+d[2]+e[2]+f[2]+g[2]
                                                        if len(sn) == len(set(sn)):
                                                            n = add_missing_digit(sn)
                                                            results[n] = n

    return sum(results)

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
