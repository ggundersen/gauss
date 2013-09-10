"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
You are given the following information, but you may prefer to do some research
for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century 
        unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?

Solution:
#TODO: I do not like relying on outside libraries. Try to improve this using
Gauss's algorithm: http://en.wikipedia.org/wiki/Determination_of_the_day_of_the
_week#Gauss.27s_algorithm 
----------------------------------------------------------------------------"""

from datetime import date


def main():

    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6: # Monday = 0,...Sunday = 6
                count += 1
    return count