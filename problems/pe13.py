"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

[see ../static/txt/pe13_numbers.txt']
----------------------------------------------------------------------------"""

import os


def main():
    
    result = 0
    path = os.path.normpath(os.path.dirname(__file__) +
        '../../txt/pe13_number.txt')

    with open(path) as f:
        lines = f.readlines()
    f.close()

    for l in lines:
        result += int(l)
    return int(str(result)[:10])