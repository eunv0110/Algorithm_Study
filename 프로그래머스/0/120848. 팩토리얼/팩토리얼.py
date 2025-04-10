def solution(n):
    num = 1
    i=2
    while True:
        num*=i
        if num>n:
            break
        i+=1

    return i-1