"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Solution:
The critical problem is finding an upper bound. This is the reasoning behind
my limit:

9! is the maximum value for any one digit
9! < 7 digits
9! * 7 is the upper bound
----------------------------------------------------------------------------"""

import lib.gmath as g


def main():

	limit = 7 * g.get_factorial(9)
	result = 0
	for n in range(3, limit):
	    if n == sum(g.get_factorial(int(i)) for i in str(n)):
	        result += n
	return result