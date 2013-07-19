def getProduct():
    prod = 0
    for i in range(999,0,-1):
        for j in range(999,0,-1):
            if isPalindrome(i*j):
                temp = i*j
                print temp
                if temp > prod:
                    print prod
                    prod = temp
    return prod

def isPalindrome(p):
    p = str(p)
    if len(p) < 2:
        return True
    elif p[0] == p[len(p)-1]:
        p = p[1:]
        p = p[:len(p)-1]
        return isPalindrome(p)
