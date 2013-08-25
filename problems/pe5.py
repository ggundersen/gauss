def main():
    incrementer = '10'
    n = int(incrementer)
    i = int(incrementer)
    while divide_by_range(n) != True:
        n += i
    return n

def divide_by_range(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True