def solution(n):
    n=list(reversed(sorted(str(n))))
    
    return int(''.join(n))