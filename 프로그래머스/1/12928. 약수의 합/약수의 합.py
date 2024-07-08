def solution(n):
    div=1
    total=[]
    while n>=div:
        x=n//div
        if n%div==0:
            total.append(x)
        div+=1
        
    return sum(total)