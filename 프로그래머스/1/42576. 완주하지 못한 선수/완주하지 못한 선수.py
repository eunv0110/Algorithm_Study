def solution(participant, completion):
    
    answer={}
    num_sum=0
    
    for p in participant:
        num=hash(p)
        answer[num]=p
        num_sum+=num
    
    for c in completion:
        num_sum-=hash(c)
    
    return answer[num_sum]
