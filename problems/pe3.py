"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Solution:
There are two optimizations.
1) We do not need to search higher than n^(1/2).
2) We do not need to search even numbers
----------------------------------------------------------------------------"""


import lib.gmath as g

def main():

    result = 0
    n = 600851475143
    for i in range(1, int(n**0.5), 2):
        if g.is_prime(i) == True and n % i == 0:
            result = i
    return result