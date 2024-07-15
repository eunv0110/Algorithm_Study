def solution(x):
    sum=0
    x2=x
    while x2>0:
        remainder=x2%10
        sum+=remainder
        x2=x2//10
    if x%sum==0:
        return True
    else:
        return False
    
        