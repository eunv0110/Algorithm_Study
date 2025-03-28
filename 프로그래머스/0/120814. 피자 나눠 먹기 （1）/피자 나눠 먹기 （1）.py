def solution(n):
    x=n//7
    y=n%7
    if y>0:
        return x+1
    else:
        return x
