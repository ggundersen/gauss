'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def main():
    limit = 100
    def sum_of_squares(limit):
        sum = 0
        for i in range(1,limit+1):
            sum += i**2
        return sum

    def square_of_sums(limit):
        sum = 0
        for i in range(1,limit+1):
            sum += i
        sum = sum**2
        return sum

    return square_of_sums(limit) - sum_of_squares(limit)