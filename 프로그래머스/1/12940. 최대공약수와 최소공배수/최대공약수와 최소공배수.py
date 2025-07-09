import math
def solution(n, m):
    #최대공약수
    num=math.gcd(n,m)
    if num==1:
        num2=n*m
    else:
        num2=n*m//num
    
    return [num,num2]