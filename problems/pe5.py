"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?

Solution:
----------------------------------------------------------------------------"""


def divide_n_by_range(n):
    
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def main():

    n = 20
    i = 10
    while divide_n_by_range(n) == False:
        n += i
    return n