'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def genPrimes():
    primes = [2]
    n = 1
    i = 1
    yield 2

    # modify this variable
    count = 10001
    
    while i < count+1:
        n += 1
        for p in primes:
            if (n % p) == 0:
                break
        else:
            primes.append(n)
            print 'prime #' + str(i)
            i += 1
            yield n

g = genPrimes()
for p in g:
    print p
