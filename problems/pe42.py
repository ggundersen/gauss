"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01-22

PROBLEM:
The nth term of the sequence of triangle numbers is given by, tn = (1/2) * n *
(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, how many are triangle words?
----------------------------------------------------------------------------"""

import lib.gmath as g
import os


def main():

    path = os.path.normpath(os.path.dirname(__file__) +
        '../../txt/pe42_words.txt')
    with open(path) as f:
        word_list = f.read().split(',')
        word_list = [word.strip('"') for word in word_list]
    f.close()

    # generate hash table of triangle numbers
    tri_hash = {}
    gen = g.gen_triangle_numbers()
    for x in range(50):
        n = gen.next()
        tri_hash[n] = [n]

    result = 0
    for word in word_list:
        if tri_hash.get(g.get_alphabet_value_word(word)) != None:
            result += 1
    return result