"""----------------------------------------------------------------------------
gmath
Gregory Gundersen

gmath a library of useful mathematical functions. The library was written as a
helper library for Project Euler. Most of the scripts were written by Gregory
Gundersen, although many of them are not original.

2013-08-24
2.1.0 - Fixed bug where is_prime(2) returned False rather than True
2.0.0 - Renaming all functions to underscore rather than camel case
      - Placing non-mathematical functions into gutils library
1.0.0 - Initial commit
----------------------------------------------------------------------------"""

import time
import gutils as u


def get_gcd(a, b):

    """Euclidean algorithm
    The power of this algorithm is that we do not have to factor.
    """

    while a:
        t = a
        a = b%a
        b = t        
    return b


def is_odd(n):

    if n % 2 == 1:
        return True
    return False


def is_prime(n):

    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    maxi = n**0.5
    i = 3
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2
    return True


def is_circular_prime(p):

    """A circular prime is a prime with the property that each number generated
    at each intermediate step when cyclically permuting its (base 10) digits is
    prime.
    """

    if not is_prime(p) or has_even_digit(p):
        return False
    for i in range(len(str(p))):
        p = u.rotate_digits(p)
        if not is_prime(p):
            return False
    return True


def gen_primes(p=2):

    """Return a generator for prime numbers, beginning at prime p
    """

    primes = [2]
    n = 1
    i = 1
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

    """Code by David Eppstein, UC Irvine, 28 Feb 2002
    Maps composites to primes witnessing their compositeness.
    This is memory efficient, as the sieve is not 'run forward'
    """

    D = {}
    q = 2   # The running integer that's checked for primeness

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

    prime_factors = []
    for p in gen_primes():
        if p*p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def is_prime_quadratic(n, a, b):
    
    if is_prime(n**2 + a*n + b):
        return True
    return False


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
        if not is_prime(n):
            yield n
            n += 1
        else:
            n += 1


def gen_composite_odd():

    yield 9
    n = 15
    while True:
        if not is_prime(n) and is_odd(n):
            yield n
            n += 2
        else:
            n += 2


def get_factorial(n):

    facts = [1, 1]
    for i in range(2, n+1):
        facts.append(facts[i-1] * i)
    return facts[n]


def factorial(n):
    
    """Classic but highly inefficient recursive function
    """
    
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
        return get_fibonacci(n-1) + get_fibonacci(n-2)


def gen_fibonacci():

    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def get_figurate(n, M):

    """
    """

    return (get_factorial(M+n-1) / get_factorial(M-1)) / get_factorial(n)


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


def is_palindromic_number(n):

    s = str(n)
    length = len(s)

    if len(s) == 1 or (len(s) == 2 and s[0] == s[1]):
        return True
    else:
        if s[0] == s[length-1]:
            s = s[1:length-1]
            return is_palindromic_number(s)
        else:
            return False


"""
def is_palindrome(n):
    s = str(n)
    r = ''.join(reversed(s))
    if s == r:
        return True
    else:
        return False
"""


def base10_to_baseK(n, k, L=[]):

    """Converts a number n from base-10 to base-k
    """

    if n == 0:
        L.reverse()
        b = map(str, L)
        b = ''.join(b)
        return int(b)
    else:
        L.append(n % k)
        return base10_to_baseK(n/k, k, L)


def is_pandigital(n):

    """A pandigital number is an integer that in a given base has among its
    significant digits each digit used in the base at least once. This function
    assumes base 10.
    """

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
    if l < 2 or not is_prime(n):
        return False
    for x in range(l):
        if not is_prime(int(s[x:])):
            return False
    for x in range(l, 0, -1):
        if not is_prime(int(s[:x])):
            return False
    return True


def is_pythagorean_triplet(a, b, c):

    if a**2 + b**2 == c**2:
        return True
    return False


def get_pythagorean_triples(p):

    """General logic:
    a+b > c ==> a+b+c > 2c ==> if 2c=p < limit, p/2 < limit
    """

    ps = []
    if p % 2 != 0:
        return None
    for a in range(1, int(p/2)):
        for b in range(a, int(p/2)):
            c = (a**2 + b**2)**0.5
            if a+b+c == p and is_pythagorean_triple([a,b,c]):
                ps.append([a,b,c])
    return ps


def get_multiplicative_order(b, n):
    
    """This function should be improved to always return a meaningful result
    e.g. It falls into an infinite loop for b = 10, n = 2 """

    k = 1
    while (b ** k) % n != 1:
        k += 1
    return k