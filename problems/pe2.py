def fibGet(n):
    if n <= 1:
        return 1
    else:
        return fibGet(n-1) + fibGet(n-2)

def fibAdd(func, maxi):
    ans = 0
    for i in range(maxi):
        if func(i) % 2 == 0:
            ans += func(i)
    return ans
        
