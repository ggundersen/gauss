'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def PE6(limit):
    def sumOfSquares(limit):
        sum = 0
        for i in range(1,limit+1):
            sum += i**2
        return sum

    def squareOfSums(limit):
        sum = 0
        for i in range(1,limit+1):
            sum += i
        sum = sum**2
        return sum

    return squareOfSums(limit) - sumOfSquares(limit)

def main():
    return PE6(100)
