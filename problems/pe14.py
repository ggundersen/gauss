"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2012-01

Problem:
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1. Which starting number, under one
million, produces the longest chain? NOTE: Once the chain starts the terms are
allowed to go above one million.
----------------------------------------------------------------------------"""


def calculate_chains(n, chains):

    if n == 1: return 1
    if n not in chains:
        chains[n] = 1 + calculate_chains(n/2 if n%2==0 else 3*n+1, chains)
    return chains[n]


def get_value(dictionary, search_value):

    for key, value in dictionary.iteritems():
        if value == search_value: return key


def main():

    chains = {}
    m = max(calculate_chains(i, chains) for i in range(1,1000000))
    return get_value(chains, m)