'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

prod = 1000
p = int(prod/2)

def isTriplet(a,b,c):
    if a**2+b**2 == c**2:
        return True
    else:
        return False

for i in range(0,p):
    for j in range(0,p):
        for k in range(0,p):
            if isTriplet(i,j,k) and i != j and i+j+k == prod:
                print i
                print j
                print k
                print i*j*k
