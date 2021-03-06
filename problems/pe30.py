"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-02

Problem:
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
----------------------------------------------------------------------------"""


def main():

    # max value for one digit is 9^p
    # max sum for whole number is p * (9^p)
    p = 5
    limit = p * (9**p)
    result = 0

    for n in range(2, limit):
        l = list(str(n))
        if n == sum(int(i)**p for i in l):
            result += n
    return result