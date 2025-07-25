def solution(participant, completion):
    answer = {}
    p_sum=0
    for p in participant:
        answer[hash(p)]=(p)
        p_sum+=hash(p)
    
    for c in completion:
        p_sum-=hash(c)
    return answer[p_sum]