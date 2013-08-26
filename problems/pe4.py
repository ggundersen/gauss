import lib.gmath as g

def main():
    prod = 0
    for i in range(999,0,-1):
        for j in range(999,0,-1):
            if g.is_palindrome(i*j):
                temp = i*j
                print temp
                if temp > prod:
                    print prod
                    prod = temp
    return prod
