"""----------------------------------------------------------------------------
gutils
Gregory Gundersen

gutils is a library created to abstract away common, useful functions for
Project Euler.

2013-08-24
1.0 - Initial commit
----------------------------------------------------------------------------"""

def is_permutation(n, m):

    return sorted(str(n)) == sorted(str(m))


def has_even_digits(n):

    if n == 0:
        return True
    while n != 0:
        if n % 2 == 0:
            return True
        n //= 10
    return False


def rotate_digits(n):

    L = list(str(n))
    f = L[0]
    for i in range(0, len(str(n))-1):
        L[i] = L[i+1]
    L[-1] = f
    return int(''.join(L))


def get_alphabet_value_char(char):

    """Return the base-1 index of a character
    """

    alphabet_values = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
        'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
        't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
    }
    return alphabet_values[char.lower()]


def get_alphabet_value_word(word):

    """Return the sum of every character in a string's base-1 index value
    """

    result = 0
    for char in word:
        result += get_alphabet_value_char(char)
    return result