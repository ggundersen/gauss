'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
import lib.gmath as g

prod = 1000
limit = int(prod/2)

def main():
    for i in range(0, limit):
        for j in range(0, limit):
            for k in range(0, limit):
                if g.is_triplet(i,j,k) and i != j and i+j+k == prod:
                    return i*j*k