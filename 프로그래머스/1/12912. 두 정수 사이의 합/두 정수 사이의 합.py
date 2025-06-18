def solution(a, b):
    if a>b:
        a,b=b,a
    answer = 0
    for num in range(a,b+1):
        answer+=num
    
    
    return answer