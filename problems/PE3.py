import gmath as g

def main(n):
    ans = 0
    i = 0
    maxi = n**0.5
    while i <= maxi:
        if g.is_prime(i) == True and n % i == 0:
            ans = i
        i += 1
    return ans
            
    

