'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import gmath

sum = 0
for i in range(1,2000001):
    if gmath.isPrime(i):
        sum += i
        
print sum
