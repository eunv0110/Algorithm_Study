def solution(n):
    
    answer = n
    
    for num in range(2,n):
        if n%num==1:
            answer=min(answer,num)
    
    return answer