def solution(n):
    sum = 0
    while n>0:
        remainder=n%10
        sum+=remainder
        n=n//10
        
    return sum