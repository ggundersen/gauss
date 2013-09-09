"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

[see ../static/txt/pe13_numbers.txt']

Solution:
----------------------------------------------------------------------------"""

import fileinput
import os

    
def main():
    
    total = 0
    path = os.path.normpath(os.path.dirname(__file__) + '../../txt/pe13_number.txt')
    # f = open(path, 'r')    this is significantly slower - why?
    for line in fileinput.input([path]):
        total += int(line)
	return int(str(total)[:10])