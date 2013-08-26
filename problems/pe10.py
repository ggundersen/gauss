'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import lib.gmath as g

sum = 0
def main():
	for i in range(1,2000001):
	    if gmath.is_prime(i):
	        sum += i
	        
	return sum
