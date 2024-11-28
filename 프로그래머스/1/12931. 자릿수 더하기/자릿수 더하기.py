def solution(n):
    answer=[]
    
    while n>0:
        remainder=n%10
        n=n//10
        answer.append(remainder)

    return sum(answer)
                
