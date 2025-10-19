def solution(n):
    res=[0,1]
    
    if n<2:
        return res[n]
    
    for i in range(2,n+1):
        res.append((res[i-1]+res[i-2])%1234567)
    return res[n]