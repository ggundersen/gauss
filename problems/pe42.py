'''
DESCRIPTION:
Project Euler, problem 42
Gregory Gundersen, 01/22/2013

PROBLEM:
The nth term of the sequence of triangle numbers is given by, tn = (1/2)*n*(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

RESOLUTION:
Solution: 162
Time: 0.0369999408722
'''
import time
import gmath as g

s = time.time()

# process file
f = open('pe42_words.txt','r')
wordList = f.read().split(',')
wordList = [word.strip('"') for word in wordList]
f.close()

# generate hash table of triangle numbers
triHash = {}
triGen = g.gen_triangle_number()
for x in range(50):
    n = triGen.next()
    triHash[n] = [n]

# main program
result = 0
for word in wordList:
    if triHash.get(g.get_alphabet_value_word(word)) != None:
        result += 1

print result
print 'Time: ' + str(time.time() - s)
