from itertools import combinations

def solution(numbers):
    result=[]
    answer=list(combinations(numbers,2))
    for i in range(len(answer)):
        answer_sum=sum(answer[i])
        result.append(answer_sum)
        result=list(set(result))
        result.sort()
    return result
    
    