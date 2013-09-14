"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-28

Problem:
In England the currency is made up of pound, L, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).

It is possible to make L2 in the following way:

    1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can L2 be made using any number of coins?

Solution:
The key idea is that this is the opposite of recursion. Rather than starting
with the biggest denomination and counting down, begin with the smallest and
count up. Think of it this way:

How many ways can you make 5p with a 1p coin? There is only one way: (5x1p).
How many ways can you make 5p with 1 and 2p coins? Two ways: (2x2p + 1x1p) and
(2x1p + 3x1p). Then add how many ways to add to 5p with a 1p coin, something
you have already calculated: a total of 3 ways. The critical point is that you
are storing your calculations as you go (dynamic programming).
----------------------------------------------------------------------------"""


def main():

    mark = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    counts = [0 for i in range(mark+1)]
    counts[0] = 1 # by convention, there is one way to make 0 coins (wiki)

    for c in range(len(coins)):
        for i in range(coins[c], mark+1):
            counts[i] += counts[i - coins[c]]
    return counts[mark]