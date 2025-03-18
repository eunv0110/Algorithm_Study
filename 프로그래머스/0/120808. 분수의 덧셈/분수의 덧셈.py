import math
def solution(numer1, denom1, numer2, denom2):
    q=denom1*denom2
    p=denom1*numer2+denom2*numer1
    
    x=math.gcd(p,q)
    if x>1:
        return [p//x,q//x]
    return [p,q]