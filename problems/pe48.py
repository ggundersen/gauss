"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
----------------------------------------------------------------------------"""


def main():

    result = 0
    for n in range(1,1001):
        result += n**n
    return int(str(result)[len(str(result))-10:])