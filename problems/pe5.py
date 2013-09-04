"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?

Solution:
Brute-force. We can iterate over 2520 because the number in question must be 
divisible by 2520 (which is divisible by 1-10).
----------------------------------------------------------------------------"""


def divide_n_by_range(n):
    
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def main():

    n = 2520
    i = 2520
    while divide_n_by_range(n) == False:
        n += i
    return n