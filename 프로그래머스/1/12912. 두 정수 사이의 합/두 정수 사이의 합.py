def solution(a, b):
    sum=0
    if b>a:
        a,b=b,a
    
    while a>=b:
        n=a-b
        sum+=b
        b+=1
    return sum
        