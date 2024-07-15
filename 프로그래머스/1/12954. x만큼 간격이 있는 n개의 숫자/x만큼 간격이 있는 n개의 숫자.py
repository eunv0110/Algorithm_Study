def solution(x, n):
    answer=[]
    count=1
    while n>=count:
        answer.append(x*count)
        count+=1
    return answer