"""----------------------------------------------------------------------------
gmath
Gregory Gundersen

The following is a library of useful mathematical functions for Project Euler.
Most of the scripts were written by Gregory Gundersen, although many of them
are not original.

2013-08-24
2.0 - Renaming all functions to underscore rather than camel case
1.0 - Initial commit
----------------------------------------------------------------------------"""

import time

def get_gcd(a, b):
    """
    Euclidean algorithm
    """
    while b:
        a = b
        b = a%b
    return a

def is_odd(n):
    if n % 2 == 1:
        return True
    return False

def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2:
        return True
    maxi = n**0.5
    i = 3
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2
    return True

def is_circular_prime(p):
    if not isPrime(p) or has_even_digit(p):
        return False
    for i in range(len(str(p))):
        p = rotate_digits(p)
        if not isPrime(p):
            return False
    return True

def gen_primes(start=2):
    primes = [2]
    n = 1
    i = 1
    yield start
    while True:
        n += 1
        for p in primes:
            if (n % p) == 0:
                break
        else:
            primes.append(n)
            yield n

def gen_primes_from_p(p):
    primes, n, i = [2], 1, 1
    yield p
    while True:
        n += 1
        for p in primes:
            if (n % p) == 0:
                break
        else:
            primes.append(n)
            yield n

def gen_sieve_of_eratosthenes():
    # Code by David Eppstein, UC Irvine, 28 Feb 2002

    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
 
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations

            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers

            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def get_prime_factors(n):
    primeFactors = []
    for p in genPrimes():
        if p*p > n:
            break
        while n % p == 0:
            primeFactors.append(p)
            n //= p
    if n > 1:
        primeFactors.append(n)

    return primeFactors

def gen_triangle_numbers():
    tri, inc = 1, 1
    yield 1
    while True:
        inc += 1
        tri += inc
        yield tri

def get_triangle_number(n):
    return (n * (n + 1)) / 2	 

def get_pentagonal_number(n):
    return (n * (3*n - 1)) / 2	 

def get_hexagonal_number(n):
    return n * (2*n - 1)

def gen_composite():
    yield 4
    n = 5
    while True:
        if not isPrime(n):
            yield n
            n += 1
        else:
            n += 1

def gen_composite_odd():
    yield 9
    n = 15
    while True:
        if not isPrime(n) and isOdd(n):
            yield n
            n += 2
        else:
            n += 2

def get_factorial(n):
    facts = [1, 1]
    for i in range(2, n+1):
        facts.append(facts[i-1] * i)
    return facts[n]

# classic but highly inefficient recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFibonacci(n-1) + getFibonacci(n-2)

def gen_fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

def get_figurate(n, M):
    return (factorial(M+n-1) / factorial(M-1)) / factorial(n)

def get_proper_divisors(n):
    divs = [1]
    for num in range(2, n/2+1):
        if n % num == 0:
            divs.append(num)
    return divs

def is_amicable_pair(a,b):
    if sum(get_proper_divisors(a)) == b and\
        sum(get_proper_divisors(b)) == a and a != b:
        return True
    return False

def is_perfect(n):
    if sum(get_proper_divisors(n)) == n:
        return True
    return False

def is_abundant(n):
    if sum(get_proper_divisors(n)) > n:
        return True
    return False

def is_deficient(n):
    if sum(get_proper_divisors(n)) < n:
        return True
    return False

def is_palindrome(n):
    sn = str(n)
    if len(sn) == 1 or (len(sn) == 2 and sn[0] == sn[1]):
        return True
    else:
        L = len(sn)-1
        if sn[0] == sn[L]:
            sn = sn[1:L]
            return is_palindrome(sn)
        else:
            return False

def base10_to_baseK(n, K, L):
    # L is an empty list
    if n == 0:
        L.reverse()
        b = map(str, L)
        b = ''.join(b)
        return int(b)
    else:
        L.append(n % K)
        return base10_to_baseK(n/K, K, L)

def is_pandigital(n):
    L = map(str, range(1, len(str(n))+1))
    for d in str(n):
        if d in L:
            L.remove(d)
        else:
            return False
    return True

def concatenated_product(n, L):
    s = ''
    for num in L:
        s += str(num * n)
    return int(s)

def is_truncatable(n):
    s = str(n)
    l = len(s)
    if l < 2 or not isPrime(n):
        return False
    for x in range(l):
        if not isPrime(int(s[x:])):
            return False
    for x in range(l, 0, -1):
        if not isPrime(int(s[:x])):
            return False
    return True

def is_pythagorean_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

def get_pythagorean_triples(p):
    ps = []
    if p % 2 != 0: return None
    # a+b > c ==> a+b+c > 2c ==> if 2c=p < limit, p/2 < limit
    for a in range(1, int(p/2)):
        for b in range(a, int(p/2)):
            c = (a**2 + b**2)**0.5
            if a+b+c == p and is_pythagorean_triple([a,b,c]):
                ps.append([a,b,c])
    return ps

def get_multiplicative_order(b, n):
    # This function should be improved to always return a meaningful result
    # e.g. It falls into an infinite loop for b = 10, n = 2
    k = 1
    while (b ** k) % n != 1:
        k += 1
    return k

# Helpers

def is_permutation(n, m):
    """ If n is a permutation of m, return True, else False
    """
    return sorted(str(n)) == sorted(str(m))

def has_even_digit(n):
    if n == 0:
        return True
    while n != 0:
        if n % 2 == 0:
            return True
        n //= 10
    return False

def rotate_digits(n):
    
    n_list = list(str(n))
    n_first = n_list[0]

    for i in range(0, len(str(n))-1):
        n_list[i] = n_list[i+1]

    n_list[-1] = n_first

    return int(''.join(n_list))

def get_alphabet_value_char(char):
    alphabet_values = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
        'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
        't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
    }
    return alphabet_values[char.lower()]

def get_alphabet_value_word(word):
    value = 0
    for char in word:
        value += get_alphabet_value_char(char)
    return value
