def solution(n):
    answer = []
    for i in range(2,n+1):
        if i%2==0:
            answer.append(i)
    answer=sum(answer)
    return answer